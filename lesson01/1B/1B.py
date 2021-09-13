n, i, j = map(int, input().split())

answer = abs(i - j) - 1

if (i <= n/2 and j <= n/2) or (i >= n/2 and j >= n/2):
    answer = abs(i - j) - 1

elif i < j:
    answer = (i - 1) + (n - j)

else:
    answer = (j - 1) + (n - i)

print(answer)
