import pytest
import json
from unittest.mock import patch, mock_open
from src.utils import load_transactions


class TestLoadTransactions:

    def test_load_valid_json(self, tmp_path):
        """Тест загрузки валичного JSON файла"""
        data = [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR"}
        ]
        file_path = tmp_path / "test.json"
        file_path.write_text(json.dumps(data))

        result = load_transactions(str(file_path))
        assert result == data
        assert len(result) == 2

    def test_load_empty_file(self, tmp_path):
        """Тест загрузки пустого файла"""
        file_path = tmp_path / "empty.json"
        file_path.write_text("")

        result = load_transactions(str(file_path))
        assert result == []

    def test_load_not_list(self, tmp_path):
        """Тест когда JSON содержит не список"""
        file_path = tmp_path / "not_list.json"
        file_path.write_text('{"key": "value"}')

        result = load_transactions(str(file_path))
        assert result == []

    def test_load_file_not_exists(self):
        """Тест когда файл не существует"""
        result = load_transactions("nonexistent.json")
        assert result == []

    def test_load_invalid_json(self, tmp_path):
        """Тест загрузки неваличного JSON"""
        file_path = tmp_path / "invalid.json"
        file_path.write_text("not valid json {")

        result = load_transactions(str(file_path))
        assert result == []