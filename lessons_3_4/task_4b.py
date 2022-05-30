"""
Формат ввода
Каждая строка входного файла содержит фамилию кандидата, за которого
отдают голоса выборщики этого штата, затем через пробел идет количество выборщиков, отдавших голоса за этого кандидата.

Формат вывода
Выведите фамилии всех кандидатов в лексикографическом порядке, затем,
через пробел, количество отданных за них голосов.
"""


with open('input_4b.txt', 'r') as f:
    lines = f.readlines()  # все остальные строки

vote_dict = {}
for line in lines:
    line = list(line.strip().split())
    candidate = line[0]
    votes = int(line[1])
    if candidate not in vote_dict.keys():
        vote_dict[candidate] = 0
    vote_dict[candidate] += votes

for key, value in sorted(vote_dict.items()):
    print(key, value)
