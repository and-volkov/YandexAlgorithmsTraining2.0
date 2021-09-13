# Lesson01 - 1A

r = int(input())  # код задачи (−128≤r≤127)
i = int(input())  # вердикт интерактора (0≤i≤7)
c = int(input())  # вердикт чекера  (0≤c≤7)
answer = ''

if i == 0:
    if r != 0:
        answer = 3
    else:
        answer = c

elif i == 1:
    answer = c

elif i == 4:
    if r != 0:
        answer = 3
    else:
        answer = 4

elif i == 6:
    answer = 0

elif i == 7:
    answer = 1

else:
    answer = i

print(answer)

