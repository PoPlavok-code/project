def add_numbers(a, b):
    return a + b


def is_even(num):
    return num % 2 == 0


def find_max(my_list):
    if len(my_list) > 0:
        return max(my_list)
    return 0


if __name__ == "__main__":
    assert add_numbers(2, 2) == 4

    assert is_even(0)  # ← то же самое, но чище и соответствует PEP 8

    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([]) == 0
