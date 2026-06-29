import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
    FilterByCurrency,
)


@pytest.fixture
def sample_transactions():
    """Список словарей-транзакций для тестов"""
    return [
        {"date": "2023-01-01", "currency": "USD", "description": "Оплата за сервис", "amount": 100},
        {"date": "2023-01-02", "currency": "RUB", "description": "Перевод другу", "amount": 5000},
        {"date": "2023-01-03", "currency": "USD", "description": "Покупка в магазине", "amount": 50},
        {"date": "2023-01-04", "currency": "EUR", "description": "Аренда", "amount": 200},
    ]


@pytest.fixture
def sample_transactions_for_class():
    """Тестовые данные для класса FilterByCurrency"""
    return [
        {
            "date": "2023-01-01",
            "operationAmount": {"amount": 100, "currency": {"code": "USD", "name": "USD"}},
            "description": "Оплата за сервис"
        },
        {
            "date": "2023-01-02",
            "operationAmount": {"amount": 5000, "currency": {"code": "RUB", "name": "руб."}},
            "description": "Перевод другу"
        },
        {
            "date": "2023-01-03",
            "operationAmount": {"amount": 50, "currency": {"code": "USD", "name": "USD"}},
            "description": "Покупка в магазине"
        },
        {
            "date": "2023-01-04",
            "operationAmount": {"amount": 200, "currency": {"code": "EUR", "name": "EUR"}},
            "description": "Аренда"
        },
    ]


# === Тесты для filter_by_currency (функция-генератор) ===

def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(t["currency"] == "USD" for t in result)


def test_filter_by_currency_rub(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["description"] == "Перевод другу"


def test_filter_by_currency_empty(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "GBP"))
    assert result == []


# === Тесты для transaction_descriptions ===

def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    expected = ["Оплата за сервис", "Перевод другу", "Покупка в магазине", "Аренда"]
    assert result == expected


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


# === Тесты для card_number_generator ===

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001"]),
        (10, 13, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_format():
    result = next(card_number_generator(1234567890123456, 1234567890123457))
    assert result == "1234 5678 9012 3456"
    assert len(result) == 19


# === Тесты для класса FilterByCurrency ===

def test_filter_by_currency_class_usd(sample_transactions_for_class):
    filter_obj = FilterByCurrency(sample_transactions_for_class)
    result = filter_obj.filter_by_currency("USD")
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_class_rub(sample_transactions_for_class):
    filter_obj = FilterByCurrency(sample_transactions_for_class)
    result = filter_obj.filter_by_currency("RUB")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод другу"


def test_filter_by_currency_class_empty(sample_transactions_for_class):
    filter_obj = FilterByCurrency(sample_transactions_for_class)
    result = filter_obj.filter_by_currency("GBP")
    assert result == []


def test_filter_by_currency_class_get_operations(sample_transactions_for_class):
    filter_obj = FilterByCurrency(sample_transactions_for_class)
    result = filter_obj.get_operations_by_currency("EUR")
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "EUR"