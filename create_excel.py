import pandas as pd

print("📖 Читаем CSV...")
df = pd.read_csv("data/transactions.csv", sep=";")
print(f"✅ Загружено из CSV: {len(df)} записей")
print(f"📋 Колонки: {df.columns.tolist()}")

print("\n💾 Сохраняем в Excel...")
df.to_excel("data/transactions_excel.xlsx", index=False, engine="openpyxl")
print("✅ Файл data/transactions_excel.xlsx создан!")

# Проверяем
print("\n🔍 Проверяем созданный файл...")
df2 = pd.read_excel("data/transactions_excel.xlsx", engine="openpyxl")
print(f"✅ В Excel файле: {len(df2)} записей")