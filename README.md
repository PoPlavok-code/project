## Генераторы данных (Модуль generators)

Этот модуль содержит инструменты для обработки массивов транзакций и генерации данных.

### Функции

#### `filter_by_currency(transactions, currency)`
Фильтрует транзакции по валюте.
**Пример:**
```python
usd_ops = filter_by_currency(transactions, "USD")
for op in usd_ops:
    print(op)