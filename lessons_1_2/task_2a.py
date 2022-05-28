"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Всего вводится не более 10000 чисел (не считая завершающего числа 0).
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

Числа, следующие за числом 0, считывать не нужно.
"""

with open('input.txt', 'r') as f:
    max_number = 0
    max_count = 0
    for number in f:
        number = int(number)
        if number != 0 and number > max_number:
            max_number = number
            max_count = 1
        elif number != 0 and number == max_number:
            max_count += 1
        elif number < max_number:
            continue
        else:
            print(max_count)

print(max_count)