"""
Дана строка S
Выведите гистограмму как в примере (коды символов отсортированы)
S = Hellow, world!

      #
      ##
##########
 !,Hdelorw
"""


def print_hist(s):
    sym_count = {}  # словарь для записи количества вхождений
    max_sym_count = 0  # максимальное кол-во вхождений
    for sym in s:
        if sym not in sym_count:
            sym_count[sym] = 0
        sym_count[sym] += 1  # записываем кол-во
        if sym_count[sym] > max_sym_count:
            max_sym_count = sym_count[sym]  # обновляем максимум

    sorted_unique_syms = sorted(sym_count.keys())  # сортируем ключи
    for row in range(max_sym_count, 0, -1):  # строки строятся от максимума
        for sym in sorted_unique_syms:
            if sym_count[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()  # перевод строки
    print(''.join(sorted_unique_syms))  # сортированные символы


test_string = 'Hello, world!'

print_hist(test_string)

"""
      #   
      ##  
##########
 !,Hdelorw
"""
