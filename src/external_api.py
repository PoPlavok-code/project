import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Сумма в рублях (float)
    """
    amount = float(transaction.get('amount', 0))
    currency = transaction.get('currency', 'RUB')

    # Если уже в рублях, возвращаем как есть
    if currency == 'RUB':
        return amount

    # Для USD и EUR делаем запрос к API
    if currency in ('USD', 'EUR'):
        api_key = os.getenv('EXCHANGE_RATES_API_KEY')
        if not api_key:
            # Если ключа нет, возвращаем исходную сумму
            return amount

        url = "https://api.apilayer.com/exchangerates_data/convert"
        headers = {
            "apikey": api_key
        }
        params = {
            "to": "RUB",
            "from": currency,
            "amount": amount
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            result = response.json()
            return float(result.get('result', amount))
        except (requests.RequestException, ValueError, KeyError):
            # При ошибке возвращаем исходную сумму
            return amount

    return amount