"""Сортировка подсчетом."""


def countsort(seq):
    min_value = min(seq)  # Минимальное значение
    max_value = max(seq)  # Максимальное значение
    k = (max_value - min_value + 1)  # Количество элементов
    count = [0] * k  # Пустой список для записи кол-ва элементов
    for item in seq:
        count[item - min_value] += 1  # запись кол-ва каждого элемента
    now_pos = 0
    for value in range(0, k):  # по всем возможным значениям (индексам)
        for i in range(count[value]):  # по значениям в ячейке
            seq[now_pos] = value + min_value
            now_pos += 1
    return seq


test_list = [2, 1, 3, 1, 3]

print(countsort(test_list))
# [1, 1, 2, 3, 3]
