import pandas as pd

print("🔍 Проверка Excel файла...")
print()

try:
    df = pd.read_excel("data/transactions_excel.xlsx", engine='openpyxl')
    print(f"✅ Успешно загружено: {len(df)} записей")
    print(f"📋 Колонки: {df.columns.tolist()}")
    print()
    if len(df) > 0:
        print("📄 Первая запись:")
        print(df.iloc[0].to_dict())
except Exception as e:
    print(f"❌ Ошибка: {e}")
    import traceback
    traceback.print_exc()