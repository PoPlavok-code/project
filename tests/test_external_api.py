import pytest
from unittest.mock import patch, MagicMock
from src.external_api import convert_to_rub


class TestConvertToRub:

    def test_convert_rub_to_rub(self):
        """Тест конвертации RUB в RUB (без изменений)"""
        transaction = {
            "amount": 100,
            "currency": "RUB"
        }
        result = convert_to_rub(transaction)
        assert result == 100.0
        assert isinstance(result, float)

    @patch('src.external_api.os.getenv')
    @patch('src.external_api.requests.get')
    def test_convert_usd_to_rub(self, mock_get, mock_getenv):
        """Тест конвертации USD в RUB"""
        # Настраиваем mock для переменной окружения
        mock_getenv.return_value = "test_api_key"

        # Настраиваем mock для запроса
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 7500.0}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        transaction = {
            "amount": 100,
            "currency": "USD"
        }
        result = convert_to_rub(transaction)

        assert result == 7500.0
        assert isinstance(result, float)
        mock_get.assert_called_once()

    @patch('src.external_api.os.getenv')
    @patch('src.external_api.requests.get')
    def test_convert_eur_to_rub(self, mock_get, mock_getenv):
        """Тест конвертации EUR в RUB"""
        mock_getenv.return_value = "test_api_key"

        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 8500.0}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        transaction = {
            "amount": 100,
            "currency": "EUR"
        }
        result = convert_to_rub(transaction)

        assert result == 8500.0
        mock_get.assert_called_once()

    @patch('src.external_api.os.getenv')
    def test_convert_no_api_key(self, mock_getenv):
        """Тест когда нет API ключа"""
        mock_getenv.return_value = None

        transaction = {
            "amount": 100,
            "currency": "USD"
        }
        result = convert_to_rub(transaction)

        assert result == 100.0  # Возвращаем исходную сумму

    @patch('src.external_api.os.getenv')
    @patch('src.external_api.requests.get')
    def test_convert_api_error(self, mock_get, mock_getenv):
        """Тест когда API возвращает ошибку"""
        mock_getenv.return_value = "test_api_key"
        # Используем ValueError вместо requests.RequestException
        mock_get.side_effect = ValueError("API Error")

        transaction = {
            "amount": 100,
            "currency": "USD"
        }
        result = convert_to_rub(transaction)

        assert result == 100.0  # Возвращаем исходную сумму при ошибке

    def test_convert_unknown_currency(self):
        """Тест с неизвестной валютой"""
        transaction = {
            "amount": 100,
            "currency": "GBP"
        }
        result = convert_to_rub(transaction)

        assert result == 100.0