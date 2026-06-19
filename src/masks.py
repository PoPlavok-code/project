import logging
import os

# Настройка логгера
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if logger.handlers:
    logger.handlers.clear()

file_handler = logging.FileHandler(
    filename=os.path.join(LOG_DIR, "masks.log"),
    mode="w",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: 1234567890123456 -> 1234 56** **** 3456"""
    logger.info("Запуск функции get_mask_card_number")
    logger.debug(f"Входной параметр: {card_number}")

    if len(card_number) != 16 or not card_number.isdigit():
        logger.error(f"Некорректный номер карты: длина={len(card_number)}")
        raise ValueError("Номер карты должен содержать 16 цифр")

    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info("Карта успешно замаскирована")
    logger.debug(f"Результат: {result}")
    return result


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта: 12345678901234567890 -> **1234"""
    logger.info("Запуск функции get_mask_account")
    logger.debug(f"Входной параметр: {account_number}")

    if len(account_number) < 4 or not account_number.isdigit():
        logger.error(f"Некорректный номер счёта: длина={len(account_number)}")
        raise ValueError("Номер счёта некорректен")

    result = f"**{account_number[-4:]}"
    logger.info("Счёт успешно замаскирован")
    logger.debug(f"Результат: {result}")
    return result