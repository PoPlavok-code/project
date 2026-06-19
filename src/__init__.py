def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: 1234567890123456 -> 1234 56** **** 3456"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта: 12345678901234567890 -> **1234"""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счёта некорректен")
    return f"**{account_number[-4:]}"
