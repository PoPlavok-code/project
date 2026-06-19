# def format_currency(amount, currency="RUB", show_symbol=True):
#     currency_symbols = {
#         "RUB": "₽",
#         "USD": "$",
#         "EUR": "€"
#     }
#
#     symbol = currency_symbols.get(currency, "")
#
#     if show_symbol:
#         return f"{symbol}{amount}"
#     else:
#         return f"{amount} {currency}"
# print(format_currency(1000))  # "1000 RUB" или "1000 ₽"
# print(format_currency(500, "USD", True))  # "$500"
# print(format_currency(750, "EUR", False))  # "750 EUR"
# from locale import currency
from itertools import count

from pycodestyle import break_before_binary_operator

# print(format_currency(1500, "RUB", True))  # "1500 ₽"
#
#
# def calculate_total(*ammounts):
#     return sum(ammounts)
# # Тесты с разным количеством аргументов
# print(calculate_total(100, 200, 300))      # 600
# print(calculate_total(50))                  # 50
# print(calculate_total())                    # 0
# print(calculate_total(10, 20, 30, 40, 50)) # 150


# def create_transaction(**kwargs):
#     """Создаёт транзакцию из именованных аргументов."""

# Проверяем наличие обязательного поля 'amount'
# if 'amount' not in kwargs:
#     raise ValueError("Сумма (amount) обязательна!")

# Добавляем статус по умолчанию
# kwargs['status'] = 'pending'

# return kwargs


# Тесты
# print(create_transaction(amount=1000, currency="USD"))
# {'amount': 1000, 'currency': 'USD', 'status': 'pending'}

# print(create_transaction(amount=500))
# {'amount': 500, 'status': 'pending'}

# print(create_transaction(currency="RUB"))  # ValueError!


# Список книг (каждая книга - словарь)
# books = [
#     {
#         "title": "Python Crash Course",
#         "author": "Eric Matthes",
#         "year": 2019,
#         "genre": "programming",
#         "rating": 4.5,
#         "copies": 3,
#         "borrowers": ["Alice", "Bob"]
#     },
#     {
#         "title": "Clean Code",
#         "author": "Robert Martin",
#         "year": 2008,
#         "genre": "programming",
#         "rating": 4.8,
#         "copies": 2,
#         "borrowers": ["Charlie"]
#     },
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "year": 1949,
#         "genre": "fiction",
#         "rating": 4.7,
#         "copies": 5,
#         "borrowers": []
#     },
#     {
#         "title": "Data Science Handbook",
#         "author": "Jake VanderPlas",
#         "year": 2016,
#         "genre": "programming",
#         "rating": 4.3,
#         "copies": 1,
#         "borrowers": ["Diana", "Eve", "Frank"]
#     },
#     {
#         "title": "The Hobbit",
#         "author": "J.R.R. Tolkien",
#         "year": 1937,
#         "genre": "fiction",
#         "rating": 4.9,
#         "copies": 4,
#         "borrowers": ["Alice"]
#     },
# ]
# copyng_books = {"Python Crash Course": 3,
#                 "Clean Code": 2,
#                 "1984": 5,
#                 "Data Science Handbook": 1,
#                 "TheHobbit": 4}
#
# total_books = sum(copyng_books.values())
# print (total_books)
#
# books_rating = [book for book in books if book.get("rating", 0) >= 4.5]
# print(books_rating)
#
#

# books_name = []
# for book in books:
#     books_name.append(book["title"])
#
# print(books_name)
#
#
# first_three_books = books[:3]
#
# # Или только их названия
# first_three_titles = [book["title"] for book in books[:3]]
# print(first_three_titles)


# books = [
#     {"title": "Python Crash Course", "genre": "programming", },
#     {"title": "Clean Code", "genre": "programming", },
#     {"title": "1984", "genre": "fiction", },
#     {"title": "Data Science Handbook", "genre": "programming", },
#     {"title": "The Hobbit", "genre": "fiction", },
# ]
#
# books_raiting_v2 = [book for book in books if book.get("genre") == "programming"]
# print(books_raiting_v2)
#


# avtor_name = [book["author"] for book in books[:5]]
# result = ",".join(avtor_name)
# print(result)

# genre_count = {}
#
# for book in books:
#     genre = book["genre"]
#     if genre in genre_count:
#         genre_count[genre] += 1
#     else:
#         genre_count[genre] = 1
#
# print(genre_count)

# def find_books_by_author(author_name):
#     find_books = []
#     for book in books:
#         if book.get("author") == author_name:
#             find_books.append(book)
#     return find_books
#
#
# print(find_books_by_author("Eric Matthes"))


# min_god = (min)(books, key=lambda x: x["year"])
#
# print(min_god)

# all_readers = set(man for book in books for man in book.get("borrowers", []))
#
# print(all_readers)


# alice_books = set()
# bob_books = set()
#
# for book in books:
#     if "Alice" in book.get("borrowers", []):
#         alice_books.add(book["title"])
#     if "Bob" in book.get("borrowers", []):
#         bob_books.add(book["title"])
#
# common_books = alice_books & bob_books
# print(common_books)
# # {'Python Crash Course'}

books = [
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "year": 2019,
        "genre": "programming",
        "rating": 4.5,
        "copies": 3,
        "borrowers": ["Alice", "Bob"]
    },
    {
        "title": "Clean Code",
        "author": "Robert Martin",
        "year": 2008,
        "genre": "programming",
        "rating": 4.8,
        "copies": 2,
        "borrowers": ["Charlie"]
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "fiction",
        "rating": 4.7,
        "copies": 5,
        "borrowers": []
    },
    {
        "title": "Data Science Handbook",
        "author": "Jake VanderPlas",
        "year": 2016,
        "genre": "programming",
        "rating": 4.3,
        "copies": 1,
        "borrowers": ["Diana", "Eve", "Frank"]
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "fiction",
        "rating": 4.9,
        "copies": 4,
        "borrowers": ["Alice"]
    },
]

alice_books = set()
bob_books = set()

for book in books:
    if "Alice" in book.get("borrowers", []):
        alice_books.add(book["title"])
    if "Bob" in book.get("borrowers", []):
        bob_books.add(book["title"])

common_books = alice_books & bob_books
print(common_books)
# {'Python Crash Course'}
