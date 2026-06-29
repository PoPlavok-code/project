import re
from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу.

    Args:
        data: Список словарей с операциями
        state: Статус для фильтрации (по умолчанию EXECUTED)

    Returns:
        Список операций с указанным статусом
    """
    return [op for op in data if op.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    Args:
        data: Список словарей с операциями
        reverse: Если True — по убыванию (новые сначала), иначе по возрастанию

    Returns:
        Отсортированный список операций

    Raises:
        ValueError: Если формат даты невалиден (но не пустой)
    """

    def parse_date(date_str: str) -> datetime:
        # Если даты нет — возвращаем минимальную дату
        if not date_str:
            return datetime.min

        try:
            return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        except (ValueError, AttributeError):
            raise ValueError(f"Невалидный формат даты: {date_str}")

    return sorted(data, key=lambda x: parse_date(x.get("date", "")), reverse=reverse)


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Ищет операции по описанию с использованием регулярных выражений.

    Args:
        data: Список словарей с операциями
        search: Строка поиска

    Returns:
        Список операций, где в описании есть искомая строка
    """
    result: List[Dict[str, Any]] = []
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    for operation in data:
        description = operation.get("description", "")
        if pattern.search(description):
            result.append(operation)

    return result


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.

    Args:
        data: Список словарей с операциями
        categories: Список названий категорий

    Returns:
        Словарь {категория: количество операций}
    """
    result: Dict[str, int] = {category: 0 for category in categories}

    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1
                break

    return result