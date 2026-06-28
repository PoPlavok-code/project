import pandas as pd

print("Проверяем Excel файл...")

# Пробуем разные варианты
try:
    # Вариант 1: с engine='xlrd' (для старых .xls файлов)
    df = pd.read_excel("data/transactions_excel.xlsx", engine='xlrd')
    print(f"✅ Строг: {len(df)}")
    print(f"Колонки: {df.columns.tolist()}")
    print(f"Первые 3 строки:")
    print(df.head(3))
except Exception as e:
    print(f" xlrd не сработал: {e}")
    try:
        # Вариант 2: с engine='openpyxl'
        df = pd.read_excel("data/transactions_excel.xlsx", engine='openpyxl')
        print(f"✅ Строг: {len(df)}")
        print(f"Колонки: {df.columns.tolist()}")
        print(df.head(3))
    except Exception as e2:
        print(f" openpyxl тоже не сработал: {e2}")