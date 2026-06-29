# src/generators.py
from typing import List, Dict, Any, Iterator


class FilterByCurrency:
    """Класс для фильтрации банковских операций по валюте."""

    def __init__(self, data: List[Dict[str, Any]]) -> None:
        """
        Инициализирует фильтр с данными.

        Args:
            data: Список словарей с банковскими операциями
        """
        self.data = data

    def filter_by_currency(self, currency: str) -> List[Dict[str, Any]]:
        """
        Фильтрует операции по коду валюты.

        Args:
            currency: Код валюты (например, 'USD', 'RUB', 'EUR')

        Returns:
            Список операций с указанной валютой
        """
        result: List[Dict[str, Any]] = []
        for operation in self.data:
            amount_data = operation.get("operationAmount", {})
            currency_data = amount_data.get("currency", {})
            if currency_data.get("code", "").upper() == currency.upper():
                result.append(operation)
        return result

    def get_operations_by_currency(self, currency: str) -> List[Dict[str, Any]]:
        """
        Возвращает все операции в заданной валюте.

        Args:
            currency: Код валюты (например, 'USD', 'RUB', 'EUR')

        Returns:
            Список операций в указанной валюте
        """
        return self.filter_by_currency(currency)


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency: str
) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по валюте (генератор).

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты для фильтрации (например, 'USD')

    Yields:
        Словари транзакций с указанной валютой
    """
    for transaction in transactions:
        if transaction.get("currency", "").upper() == currency.upper():
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]],
) -> Iterator[str]:
    """
    Возвращает описания транзакций (генератор).

    Args:
        transactions: Список словарей с транзакциями

    Yields:
        Строки описаний транзакций
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: Начальный номер карты
        stop: Конечный номер карты (не включается)

    Yields:
        Строки с номерами карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, stop):
        card_str = str(number).zfill(16)
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"