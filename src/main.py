import math


def calculate_logarithm(number: float, base: float) -> float:
    """Вычисляет логарифм числа по заданному основанию."""
    if number <= 0 or base <= 0 or base == 1:
        raise ValueError("Число и основание должны быть положительными, основание не равно 1")
    return math.log(number, base)


def finder(lst: list, data_type: type) -> float:
    """Возвращает долю элементов заданного типа в списке."""
    if not lst:
        return 0.0
    count = sum(1 for item in lst if isinstance(item, data_type))
    return count / len(lst)


def reverse_string(s: str) -> str:
    """Разворачивает строку."""
    return s[::-1]
