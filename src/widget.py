from src.masks import get_mask_card_number, get_mask_account,
from typing datetime


def mask_account_card(card_string: str) -> str:
    """
    Маскирует номер карты или счёта из одной строки.
    Пример:
        'Visa Platinum 7000792289606361' -> 'Visa Platinum 7000 79** **** 6361'
        'Счет 73654108430135874305' -> 'Счет **4305'
    """
    parts = card_string.split()
    number = parts[-1]  # Последний элемент всегда номер
    card_type = " ".join(parts[:-1])  # Всё остальное - тип
    if card_type.lower() == "счет":
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)
    return f"{card_type} {masked}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку даты в формат ДД.ММ.ГГГГ.
    Пример: '2024-03-11T02:26:18.671407' -> '11.03.2024'
    """
    # datetime.fromisoformat() автоматически понимает формат ISO 8601
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
