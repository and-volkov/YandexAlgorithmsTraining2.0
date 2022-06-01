"""
Даны три массива целых чисел A, B, C и целое число S.
Найдите такие i, j, k, что A.i + B.j + C.k = S.

Формат ввода
На первой строке число S (1 ≤ S ≤ 10**9).
Следующие три строки содержат описание массивов A, B, C в одинаковом формате: первое число задает длину n
соответствующего массива (1 ≤ n ≤ 15000), затем заданы n целых чисел от
1 до 10**9 — сам массив.
Формат вывода
Если таких i, j, k не существует, выведите единственное число −1.
Иначе выведите на одной строке три числа — i, j, k.
Элементы массивов нумеруются с нуля. Если ответов несколько, выведите лексикографически минимальный.
"""

s = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


c_dict = {}
for index, element in enumerate(c[1:]):
    if element not in c_dict:
        c_dict[element] = index


def find_sum(s, a, b, c_dict):

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            value_in_dict = s - a[i] - b[j]
            if value_in_dict in c_dict:
                return f'{i - 1} {j - 1} {c_dict[value_in_dict]}'
    return -1


print(find_sum(s, a, b, c_dict))
