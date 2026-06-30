import os
import sys
from typing import List, Dict, Any
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_transactions, load_transactions_from_csv, load_transactions_from_excel
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date, process_bank_search


def format_date(date_str: str) -> str:
    """Форматирует дату из ISO формата в DD.MM.YYYY."""
    if not isinstance(date_str, str) or not date_str:
        return ""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%d.%m.%Y')
    except Exception:
        return str(date_str)[:10]


def format_account(account) -> str:
    """Маскирует номер счета или карты."""
    if not isinstance(account, str) or not account:
        return ""

    parts = account.split()
    if len(parts) < 2:
        return account

    account_type = parts[0]
    account_number = parts[-1]

    if account_type == "Счет":
        return f"Счет {get_mask_account(account_number)}"
    else:
        return f"{account_type} {get_mask_card_number(account_number)}"


def get_currency_name(transaction: Dict[str, Any]) -> str:
    """
    Получает название валюты из транзакции (универсально для JSON и CSV/XLSX).

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Название валюты (руб., USD, EUR и т.д.)
    """
    # Для CSV/XLSX - поле currency_name на верхнем уровне
    if "currency_name" in transaction:
        return str(transaction.get("currency_name", ""))

    # Для JSON - поле внутри operationAmount
    if "operationAmount" in transaction:
        amount_data = transaction.get("operationAmount", {})
        if isinstance(amount_data, dict):
            currency_data = amount_data.get("currency", {})
            if isinstance(currency_data, dict):
                return str(currency_data.get("name", ""))

    return ""


def get_currency_code(transaction: Dict[str, Any]) -> str:
    """
    Получает код валюты из транзакции (универсально для JSON и CSV/XLSX).

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Код валюты (RUB, USD, EUR и т.д.)
    """
    # Для CSV/XLSX - поле currency_code на верхнем уровне
    if "currency_code" in transaction:
        return str(transaction.get("currency_code", ""))

    # Для JSON - поле внутри operationAmount
    if "operationAmount" in transaction:
        amount_data = transaction.get("operationAmount", {})
        if isinstance(amount_data, dict):
            currency_data = amount_data.get("currency", {})
            if isinstance(currency_data, dict):
                return str(currency_data.get("code", ""))

    return ""


def get_amount(transaction: Dict[str, Any]) -> float:
    """
    Получает сумму транзакции (универсально для JSON и CSV/XLSX).

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Сумма транзакции
    """
    # Для CSV/XLSX - поле amount на верхнем уровне
    if "amount" in transaction:
        try:
            return float(transaction.get("amount", 0))
        except (ValueError, TypeError):
            return 0.0

    # Для JSON - поле внутри operationAmount
    if "operationAmount" in transaction:
        amount_data = transaction.get("operationAmount", {})
        if isinstance(amount_data, dict):
            try:
                return float(amount_data.get("amount", 0))
            except (ValueError, TypeError):
                return 0.0

    return 0.0


def main() -> None:
    """Основная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nВаш выбор: ").strip()

    if choice == "1":
        print("\nДля обработки выбран JSON-файл.")
        transactions: List[Dict[str, Any]] = load_transactions("data/operations.json")
    elif choice == "2":
        print("\nДля обработки выбран CSV-файл.")
        transactions = load_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        print("\nДля обработки выбран XLSX-файл.")
        transactions = load_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор!")
        return

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")
        status = input("\nВаш выбор: ").strip().upper()

        if not status:
            print("Пожалуйста, введите статус!")
            continue

        if status in valid_statuses:
            transactions = filter_by_state(transactions, status)
            print(f'\nОперации отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'\nСтатус операции "{status}" недоступен.')

    # Сортировка по дате
    sort_by_date_input = input("\nОтсортировать операции по дате? Да/Нет: ").strip().lower()

    if sort_by_date_input in ["да", "д", "yes", "y"]:
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = "убыв" in sort_order
        transactions = sort_by_date(transactions, reverse=reverse)

    # Фильтр по валюте (рубли)
    rub_only = input("\nВыводить только рублевые транзакции? Да/Нет: ").strip().lower()

    if rub_only in ["да", "д", "yes", "y"]:
        # Фильтруем по названию или коду валюты
        filtered_transactions = []
        for t in transactions:
            currency_name = get_currency_name(t).lower()
            currency_code = get_currency_code(t).upper()
            # Проверяем и название (руб., ruble), и код (RUB)
            if currency_name in ["руб.", "ruble", "rub"] or currency_code == "RUB":
                filtered_transactions.append(t)
        transactions = filtered_transactions

    # Поиск по описанию
    search = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()

    if search in ["да", "д", "yes", "y"]:
        search_str = input("Введите слово для поиска: ").strip()
        transactions = process_bank_search(transactions, search_str)

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

        for transaction in transactions:
            date = format_date(transaction.get("date", ""))
            description = transaction.get("description", "")
            from_account = format_account(transaction.get("from", ""))
            to_account = format_account(transaction.get("to", ""))
            amount = get_amount(transaction)
            currency = get_currency_name(transaction)

            print(f"{date} {description}")
            if from_account and to_account:
                print(f"{from_account} -> {to_account}")
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()