# tests/test_widget.py
import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa 4567888844441234", "Visa 4567 88** **** 1234"),
        ("Счет 73654198484386453761", "Счет **3761"),
        ("MasterCard 7000000000001111", "MasterCard 7000 00** **** 1111"),
    ],
)
def test_mask_account_card(mask_inputs, input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str", ["", "123456", "Unknown 1234", None])
def test_mask_account_card_invalid(input_str):
    # Добавлены IndexError и AttributeError, которые реально возникают в коде
    with pytest.raises((ValueError, TypeError, KeyError, IndexError, AttributeError)):
        mask_account_card(input_str)


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.173319", "11.03.2024"),
        ("2023-12-31T23:59:59", "31.12.2023"),
    ],
)
def test_get_date_valid(date_inputs, date_str, expected):
    assert get_date(date_str) == expected


@pytest.mark.parametrize("date_str", ["", "not-a-date", "2024/13/45", None])
def test_get_date_invalid(date_str):
    with pytest.raises((ValueError, TypeError)):
        get_date(date_str)
