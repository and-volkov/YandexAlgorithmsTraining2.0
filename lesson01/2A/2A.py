numbers = []

with open('input.txt') as f:
    for line in f:
        integer = [int(i) for i in line.split()]
        if integer[0] != 0:
            numbers.append(integer[0])
        else:
            break

if len(numbers) != 0:
    max_value = max(numbers)
    count = numbers.count(max_value)
    print(count)
else:
    print(0)
