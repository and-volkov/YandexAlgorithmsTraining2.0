"""
На прямой в точках a.1, a.2, … , a.n (возможно, совпадающих) сидят n котят.
На той же прямой лежат m отрезков [l.1, r.1], [l.2, r.2], …, [l.m, r.m].
Нужно для каждого отрезка узнать его наполненность котятами — сколько котят сидит на отрезке.
Формат ввода
На первой строке n и m (1 ≤ n, m ≤ 10**5). На второй строке n целых чисел
a.i (0 ≤ a.i ≤ 10**9). Следующие m строк содержат пары целых чисел
l.i, r.i (0 ≤ l.i ≤ r.i ≤ 10**9).
Формат вывода
Выведите m целых чисел. i-е число — наполненность котятами i-го отрезка.
"""

START = -1
CAT = 0
END = 1

n, m = map(int, input().split())
cats = list(map(int, input().split()))

events = []

for i in range(m):
    line_start, line_end = map(int, input().split())
    events.append((line_start, START, i))  # добавляем номер отрезка
    events.append((line_end, END, i))

for cat_position in cats:
    events.append((cat_position, CAT))

cats_for_line = [0] * m  # список результатов

events.sort()
cats_count = 0  # счетчик котиков

# количество котиков на отрезке -
# разница между общим счетчик и кол-вом в начале отрезка
for i in range(len(events)):
    if events[i][1] == -1:
        cats_for_line[events[i][2]] = cats_count
    elif events[i][1] == 1:
        cats_for_line[events[i][2]] = cats_count - cats_for_line[events[i][2]]
    elif events[i][1] == 0:
        cats_count += 1

print(*cats_for_line)
