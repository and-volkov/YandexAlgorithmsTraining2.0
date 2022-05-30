"""
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке. Указание.
После того, как вы создадите словарь всех слов, вам захочется отсортировать его по
частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами
которого будут кортежи из двух элементов: частота встречаемости слова и само слово.
Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей,
при этом кортежи сравниваются по первому элементу, а если они равны — то по второму. Это почти то, что требуется в задаче.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.
"""
from operator import itemgetter

with open('input_4c.txt', 'r') as f:
    lines = f.readlines()  # все остальные строки

words_dict = {}
for line in lines:
    line = list(line.strip().split())
    for word in line:
        if word not in words_dict.keys():
            words_dict[word] = 0
        words_dict[word] += 1

ans_list = []
for key, value in words_dict.items():
    ans_list.append((value, key))

ans_list = sorted(ans_list, key=itemgetter(1))
ans_list = sorted(ans_list, key=itemgetter(0), reverse=True)
for answer in ans_list:
    print(answer[1])
