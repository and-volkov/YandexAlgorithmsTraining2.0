#  после разбора
#  рассадить учеников по аудиториям с достаточным кол-вом компов
#  + комп для препода

def read_and_enum():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        x[i] = (x[i], i + 1)  # запомнить номера аудиторий
    x.sort()
    return x


n, m = map(int, input().split())  # n-групп, m-аудиторий
x = read_and_enum()  # x.i человек в каждой аудитории
y = read_and_enum()  # y.i компьютеров в каждой аудитории

y_num = 0  # номер аудитории для итерации
ans = [0] * (n + 1)  # нули будут означать, что в аудиторию никого не посадить
cnt = 0

for people, x_num in x:
    while y_num < len(y) and y[y_num][0] < people + 1:
        y_num += 1
    if y_num == len(y):
        break
    ans[x_num] = y[y_num][1]  # аудитория для группы
    y_num += 1
    cnt += 1

print(cnt)
print(*ans[1:])  # т.к. первый элемент пустой
