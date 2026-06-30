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
    # Защита от NaN, None, float, int и других нестроковых типов
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

    # Фильтр по валюте
    rub_only = input("\nВыводить только рублевые транзакции? Да/Нет: ").strip().lower()

    if rub_only in ["да", "д", "yes", "y"]:
        transactions = [
            t for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("name") == "руб."
        ]

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
            amount_data = transaction.get("operationAmount", {})
            amount = amount_data.get("amount", 0)
            currency = amount_data.get("currency", {}).get("name", "руб.")

            print(f"{date} {description}")
            if from_account and to_account:
                print(f"{from_account} -> {to_account}")
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()