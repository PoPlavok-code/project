import pytest

from src.main import calculate_logarithm, finder, reverse_string

# ... другие функции ...


def test_calculate_logarithm():
    assert calculate_logarithm(8, 2) == 3.0
    with pytest.raises(ValueError):
        calculate_logarithm(-8, 2)
    with pytest.raises(ValueError):
        calculate_logarithm(8, 1)
    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)


def test_reverse_string_ling():  # ← БЕЗ ПАРАМЕТРОВ!
    assert reverse_string("123") == "321"  # ← замени 'ling' на ожидаемое значение


def test_reverse_string_long():  # ← БЕЗ ПАРАМЕТРОВ!
    assert reverse_string("hello") == "olleh"  # ← замени 'long' на ожидаемое значение


def test_finder_basic():  # ← НА ВЕРХНЕМ УРОВНЕ!
    assert abs(finder([1, "hello", 2.5], str) - 1 / 3) < 1e-9
    assert finder([1, 2, 3], str) == 0
