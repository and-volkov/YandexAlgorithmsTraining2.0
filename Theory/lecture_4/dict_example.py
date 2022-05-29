"""
На шахматной доске NxN находятся М ладей (ладья бьет клетки на той же
горизонтали или вертикали до ближайшей занятой)

Определите, сколько пар ладей бьют друг друга.
Ладьи задаются парой чисел I и J, обозначающих координаты клетки

1 <= N <= 10**9, 0 <= M <= 2 * 10**5
"""

# Т.к. N очень большое, будем использовать значения координат ладей.
# Пар всегда на одну меньше, чем количество ладей на горизонтали или вертикали


def count_rook_pairs(rook_coords):
    def add_rook(row_or_col, key):  # добавление координат в словарь
        if key not in row_or_col:  # если ключа нет - создадим
            row_or_col[key] = 0
        row_or_col[key] += 1  # прибавим если ключ есть

    def count_pairs(row_or_col):
        pairs = 0
        for key in row_or_col.keys():
            pairs += row_or_col[key]
        return pairs

    rooks_in_row = {}
    rooks_in_col = {}
    for row, col in rook_coords:
        add_rook(rooks_in_row, row)
        add_rook(rooks_in_col, col)
    return count_pairs(rooks_in_row) + count_pairs(rooks_in_col)
