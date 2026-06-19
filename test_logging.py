from src.masks import get_mask_card_number, get_mask_account
from src.utils import load_transactions


def main() -> None:
    # Тест маскировки карты
    print(get_mask_card_number("1234567890123456"))
    print(get_mask_account("12345678901234567890"))

    # Тест загрузки транзакций
    transactions = load_transactions("data/operations.json")
    print(f"Загружено транзакций: {len(transactions)}")


if __name__ == "__main__":
    main()