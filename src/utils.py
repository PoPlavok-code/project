import json
import logging
import os
from typing import List, Dict, Any

# Настройка логгера
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if logger.handlers:
    logger.handlers.clear()

file_handler = logging.FileHandler(
    filename=os.path.join(LOG_DIR, "utils.log"),
    mode="w",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON файла."""
    logger.info(f"Загрузка транзакций из файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Явная проверка типа для mypy
        if isinstance(data, list):
            logger.info(f"Успешно загружено {len(data)} транзакций")
            return data  # type: ignore[return-value]
        else:
            logger.warning(f"Ожидался список, получено: {type(data)}")
            return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка чтения JSON в файле: {file_path}")
        return []