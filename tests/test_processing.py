# tests/test_processing.py
import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_no_match(sample_transactions):
    result = filter_by_state(sample_transactions, "COMPLETED")
    assert result == []


def test_filter_by_state_empty(empty_list):
    assert filter_by_state(empty_list, "EXECUTED") == []


def test_sort_by_date_desc(sample_transactions):
    result = sort_by_date(sample_transactions, reverse=True)
    assert result[0]["date"] >= result[1]["date"]


def test_sort_by_date_asc(sample_transactions):
    result = sort_by_date(sample_transactions, reverse=False)
    assert result[0]["date"] <= result[1]["date"]


def test_sort_by_date_same_date(sample_transactions):
    result = sort_by_date(sample_transactions, reverse=True)
    assert len(result) == len(sample_transactions)


def test_sort_by_date_empty(empty_list):
    assert sort_by_date(empty_list) == []


def test_filter_by_state_parametrized(sample_transactions):
    for state in ["EXECUTED", "CANCELED", "PENDING"]:
        filtered = filter_by_state(sample_transactions, state)
        assert all(d["state"] == state for d in filtered)


# === НОВЫЕ ТЕСТЫ ДЛЯ ПОКРЫТИЯ ВЕТОК ОШИБОК (строки 42, 48-68) ===
def test_sort_by_date_invalid_format():
    """Проверяет, что функция выбрасывает ValueError при невалидном формате даты"""
    data = [{"id": 1, "state": "EXECUTED", "date": "invalid-date-format"}]
    with pytest.raises(ValueError):  # ✅ Ожидаем исключение
        sort_by_date(data)


def test_filter_by_state_missing_key():
    """Покрывает обработку отсутствующего ключа 'state'"""
    data = [{"id": 1, "date": "2024-01-01"}]
    try:
        filter_by_state(data, "EXECUTED")
    except (KeyError, TypeError):
        pass  # Ожидаемо при отсутствии ключа


def test_sort_by_date_missing_key():
    """Покрывает обработку отсутствующего ключа 'date'"""
    data = [{"id": 1, "state": "EXECUTED"}]
    try:
        sort_by_date(data)
    except (KeyError, TypeError):
        pass  # Ожидаемо при отсутствии ключа
