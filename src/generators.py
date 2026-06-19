# src/generators.py


class FilterByCurrency:
    """Итератор для фильтрации транзакций по валюте."""

    def __init__(self, transactions, currency):
        self.transactions = transactions
        self.currency = currency
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.transactions):
            transaction = self.transactions[self.index]
            self.index += 1
            if transaction.get("currency") == self.currency:
                return transaction
        raise StopIteration


# Для обратной совместимости можно оставить функцию-обертку
def filter_by_currency(transactions, currency):
    """
    Возвращает итератор для фильтрации транзакций по валюте.
    """
    return FilterByCurrency(transactions, currency)


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction.get("description", "Неизвестная операция")


def card_number_generator(start, stop):
    """
    Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX в заданном диапазоне.
    """
    for num in range(start, stop):
        # Превращаем число в строку и дополняем нулями до 16 символов
        card_str = str(num).zfill(16)
        # Форматируем с пробелами: 0000 0000 0000 0001
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted
