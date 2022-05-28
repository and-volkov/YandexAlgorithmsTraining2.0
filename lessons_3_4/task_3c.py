"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
"""

input_list = list(map(int, input().split()))


def find_unique_items(items_list: list) -> list:
    count_dict = {}
    for item in items_list:
        if item not in count_dict.keys():
            count_dict[item] = 1
        else:
            count_dict[item] += 1
    ans = [str(key) for key in count_dict.keys() if count_dict[key] == 1]
    print(' '.join(ans))


find_unique_items(input_list)
