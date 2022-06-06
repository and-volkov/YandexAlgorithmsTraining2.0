"""
Формат ввода
На первой строке входного файла задано число N (0 ≤ N ≤ 50 000).
На следующих N строках находится по 2 целых положительных числа Ti и Li – время прибытия
соответствующего груза и время, требуемое для его обработки (1 ≤ Ti ≤ 106, 1 ≤ Li ≤ 106).

Формат вывода
В выходной файл выведите одно число – наименьшее количество аппаратов,
которое нужно установить, чтобы не вызвать подозрений у Министерства.
Аппарат может проверять только одну коробку
"""

BOX_IN = 1
BOX_OUT = -1


n = int(input())
boxes = []

for item in range(n):
    box = list(map(int, input().split()))
    boxes.append((box[0], BOX_IN))
    boxes.append((box[0] + box[1], BOX_OUT))

boxes.sort()
device_counter = 0
max_devices = 0

for i in range(len(boxes)):
    if boxes[i][1] == -1:
        device_counter -= 1
    else:
        device_counter += 1
    max_devices = max(device_counter, max_devices)

print(max_devices)
