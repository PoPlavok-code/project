"""Модуль для обработки банковских операций."""

from datetime import datetime


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список операций по заданному статусу.

    Args:
        data: Список словарей с данными об операциях.
        state: Статус операции (по умолчанию 'EXECUTED').

    Returns:
        Список словарей, соответствующих заданному статусу.
    """
    if not data:
        return []

    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Сортирует список операций по дате.

    Args:
        data: Список словарей с данными об операциях.
        reverse: Порядок сортировки
        (True — по убыванию, False — по возрастанию).

    Returns:
        Отсортированный список словарей.
    """
    if not data:
        return []

    def get_date_key(item: dict) -> datetime:
        date_str = item.get("date")
        if date_str:
            return datetime.fromisoformat(date_str)
        return datetime.min

    return sorted(data, key=get_date_key, reverse=reverse)


if __name__ == "__main__":
    operations = [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print("--- Тест filter_by_state ---")
    executed = filter_by_state(operations)
    print(f"Найдено EXECUTED: {len(executed)} шт.")
    print(executed)

    canceled = filter_by_state(operations, "CANCELED")
    print(f"\nНайдено CANCELED: {len(canceled)} шт.")
    print(canceled)

    print("\n--- Тест sort_by_date ---")
    sorted_ops = sort_by_date(operations)
    print("Сортировка по убыванию (сначала 2019 год):")
    for op in sorted_ops:
        print(f"{op['date']} | {op['state']}")
