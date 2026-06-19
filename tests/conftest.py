# import pytest
#
#
# @pytest.fixture
# def ling():
#     return "321"
#
#
# @pytest.fixture
# def long():
#     return "olleh"


# tests/conftest.py
import pytest


# === Фикстуры для masks ===
@pytest.fixture
def valid_card_numbers():
    return ["4567888844441234", "7000000000001111", "1234567890123456"]


@pytest.fixture
def invalid_card_numbers():
    return ["", "1234", "abcd", None, "12345678901234567890"]


@pytest.fixture
def valid_account_numbers():
    return ["73654198484386453761", "12345678901234567890"]


@pytest.fixture
def invalid_account_numbers():
    return ["", "12345", None, "9876543210123456789012345"]


# === Фикстуры для widget ===
@pytest.fixture
def mask_inputs():
    return [
        ("Visa 4567888844441234", "Visa 4567 88** **** 1234"),
        ("Счет 73654198484386453761", "Счет **3761"),
        ("MasterCard 7000000000001111", "MasterCard 7000 00** **** 1111"),
    ]


@pytest.fixture
def invalid_mask_inputs():
    return ["", "123456", "Unknown 1234", None]


@pytest.fixture
def date_inputs():
    return [
        ("2024-03-11T02:26:18.173319", "11.03.2024"),
        ("2023-12-31T23:59:59", "31.12.2023"),
    ]


@pytest.fixture
def invalid_date_inputs():
    return ["", "not-a-date", "2024/13/45", None]


# === Фикстуры для processing ===
@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-15T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-31T18:30:00"},
        {"id": 4, "state": "PENDING", "date": "2024-03-11T02:26:18"},
    ]


@pytest.fixture
def empty_list():
    return []
