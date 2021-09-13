d = int(input())
x = list(map(int, input().split()))

a = [0, 0]
b = [d, 0]
c = [0, d]

min_a = (abs(x[0] - a[0]) + abs(x[1] - a[1]))
min_b = (abs(x[0] - b[0]) + abs(x[1] - b[1]))
min_c = (abs(x[0] - c[0]) + abs(x[1] - c[1]))
min_list = [min_a, min_b, min_c]

if ((x[0] <= d and x[1] <= d/2) or (x[1] <= d and x[0] <= d/2)) and (x[0] >= 0 and x[1] >= 0):
    print(0)

else:
    index_min = min(range(len(min_list)), key=min_list.__getitem__)
    print(index_min + 1)
