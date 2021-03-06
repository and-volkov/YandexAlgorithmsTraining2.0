"""
Формат ввода
Первая строка входных данных содержит число n — наибольшее число,
которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
Каждая строка представляет собой набор чисел, разделенных пробелами.
После каждой строки с вопросом идет ответ Августа: YES или NO. Наконец,
последняя строка входных данных содержит одно слово HELP.

Формат вывода
Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.
"""
# После разбора

n = int(input())
possible = set(range(1, n + 1))
s = input().strip()

while s != 'HELP':
    nums = set(map(int, s.split()))  # строка с числами
    s = input().strip()  # строка с ответом Августа
    if s == 'YES':
        possible.intersection_update(nums)
    else:
        possible.difference_update(nums)
    s = input().strip()

print(*sorted(possible))
