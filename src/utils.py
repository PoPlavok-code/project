import json
import os
from typing import List, Dict, Any


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON файла.

    Args:
        file_path: Путь к JSON файлу

    Returns:
        Список словарей с транзакциями или пустой список при ошибке
    """
    try:
        if not os.path.exists(file_path):
            return []

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, IOError, OSError):
        return []