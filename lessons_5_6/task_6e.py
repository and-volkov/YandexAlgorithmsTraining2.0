"""
Даны n точек на прямой, нужно покрыть их k отрезками одинаковой
длины ℓ.
Найдите минимальное ℓ.

Формат ввода
На первой строке n (1 ≤ n ≤ 10**5) и k (1 ≤ k ≤ n).
На второй n чисел x.i (∣x.i∣ ≤ 10**9).
Формат вывода
Минимальное такое ℓ, что точки можно покрыть k отрезками длины ℓ.
"""

# после разбора

n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

left = 0
right = x[-1] - x[0]

while left < right:
    len_of_segment = (right + left) // 2
    cnt = 0
    max_right = x[0] - 1
    for now_x in x:
        if now_x > max_right:
            cnt += 1
            max_right = now_x + len_of_segment
    if cnt <= k:
        right = len_of_segment
    else:
        left = len_of_segment + 1

print(left)
