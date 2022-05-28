"""
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO, если не встречалось.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
"""

input_list = list(map(int, input().split()))


def search_occurrence(items_list: list):
    items = set()
    for item in items_list:
        if item not in items:
            items.add(item)
            print('NO')
        else:
            print('YES')


search_occurrence(input_list)
