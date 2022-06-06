"""
На числовой прямой окрасили N отрезков.
Известны координаты левого и правого концов каждого отрезка (Li и Ri).
Найти длину окрашенной части числовой прямой.

Формат ввода
В первой строке находится число N, в следующих N строках - пары Li и Ri.
Li и Ri - целые, -10**9 ≤ Li ≤ Ri ≤ 10**9, 1 ≤ N ≤ 15 000

Формат вывода
Вывести одно число - длину окрашенной части прямой.
"""

START_LINE = -1
END_LINE = 1

n = int(input())
paint_lines = []

for item in range(n):
    line = list(map(int, input().split()))
    paint_lines.append((line[0], START_LINE))
    paint_lines.append((line[1], END_LINE))

paint_lines.sort()
painted = 0
line_count = 0


for i in range(len(paint_lines)):
    if line_count > 0:
        painted += paint_lines[i][0] - paint_lines[i - 1][0]
    if paint_lines[i][1] == -1:
        line_count += 1
    else:
        line_count -= 1

print(painted)
