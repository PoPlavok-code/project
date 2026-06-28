import json
import logging
import os
from typing import List, Dict, Any, cast

import pandas as pd

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

        if isinstance(data, list):
            logger.info(f"Успешно загружено {len(data)} транзакций")
            return cast(List[Dict[str, Any]], data)
        else:
            logger.warning(f"Ожидался список, получено: {type(data)}")
            return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка чтения JSON в файле: {file_path}")
        return []


def load_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из CSV файла."""
    logger.info(f"Загрузка транзакций из CSV: {file_path}")

    try:
        df = pd.read_csv(file_path, sep=";")
        result = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        logger.info(f"Успешно загружено {len(result)} записей из CSV")
        return result
    except FileNotFoundError:
        logger.error(f"CSV файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка чтения CSV: {e}")
        return []


def load_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из XLSX файла."""
    logger.info(f"Загрузка транзакций из Excel: {file_path}")

    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        result = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        logger.info(f"Успешно загружено {len(result)} записей из Excel")
        return result
    except FileNotFoundError:
        logger.error(f"Excel файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка чтения Excel: {e}")
        return []