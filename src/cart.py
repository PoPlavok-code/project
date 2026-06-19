# Список товаров, которые купил покупатель
cart = ["apple", "bread", "milk", "apple", "chocolate"]

# Словарь с ценами (цена за 1 штуку)
prices = {"apple": 50, "bread": 30, "milk": 80, "chocolate": 120}
total_price = 0
seen_items: dict[str, int] = {}

for item in cart:
    if item in seen_items:
        seen_items[item] += 1
    else:
        seen_items[item] = 1
    # проверяем какой по счету товар
    if seen_items[item] == 1:
        total_price += prices[item]
    else:
        total_price += prices[item] // 2

print(total_price)
