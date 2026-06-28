from src.utils import load_transactions_from_csv, load_transactions_from_excel

print("Тестируем CSV...")
csv_data = load_transactions_from_csv("data/transactions.csv")
print(f"CSV: Загружено {len(csv_data)} записей")
if csv_data:
    print(f"Пример: {csv_data[0]}")

print()
print("Тестируем Excel...")
excel_data = load_transactions_from_excel("data/transactions_excel.xlsx")
print(f"Excel: Загружено {len(excel_data)} записей")
if excel_data:
    print(f"Пример: {excel_data[0]}")