x, y, z = map(int, input().split())

if x == y:
    print(1)
elif x <= 12 < y:
    print(1)
elif y <= 12 < x:
    print(1)
else:
    print(0)
