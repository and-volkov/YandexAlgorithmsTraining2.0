"""
В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой.
Формат ввода
В первой строке входных данных записано единственное число
n (1 ≤ n ≤ 3 * 10**5) - размер массива.
Во второй строке записано n целых чисел a.i (−10**9 ≤ a.i ≤ 10**9) - сам массив.

Формат вывода
Выведите одно число - максимальную сумму на отрезке в данном массиве.
"""

n = int(input())
min_pref_sum_i = 0

nums = list(map(int, input().split()))
max_sum = nums[0]

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    if prefix_sum[i - 1] < prefix_sum[min_pref_sum_i]:
        min_pref_sum_i = i - 1

    current_sum = prefix_sum[i] - prefix_sum[min_pref_sum_i]

    if max_sum < current_sum:
        max_sum = current_sum

print(max_sum)
