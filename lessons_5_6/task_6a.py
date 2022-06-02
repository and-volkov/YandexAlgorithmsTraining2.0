"""
Дан массив из N целых чисел. Все числа от −10**9 до 10**9.
Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от
L до R?”.

Формат ввода
Число N (1 ≤ N ≤ 10**5). Далее N целых чисел.
Затем число запросов K (1 ≤ K ≤ 10**5).
Далее K пар чисел L, R (−10**9 ≤ L ≤ R ≤ 10**9) — собственно запросы.

Формат вывода
Выведите K чисел — ответы на запросы.
"""


n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

k = int(input())
results = []

for i in range(k):
    start, end = map(int, input().split())
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= start:
            right = mid
        else:
            left = mid + 1
    result_left = left
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] <= end:
            left = mid
        else:
            right = mid - 1
    result_right = left
    if end < nums[left] or start > nums[right]:
        results.append(0)
    else:
        results.append((result_right - result_left) + 1)

print(' '.join(map(str, results)))
