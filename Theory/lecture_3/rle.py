"""Реализовать алгоритм сжатия (RLE - run length encoding)"""

target_string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBB'

# easy mod - оставляем буквы по одному разу


def easy_rle(s: str) -> str:
    last_symbol = s[0]
    ans = []
    for i in range(len(s)):
        if s[i] != last_symbol:  # если не совпадают, то записываем предыдущий
            ans.append(last_symbol)
            last_symbol = s[i]  # запоминаем новый символ
    ans.append(last_symbol)  # добавляем последний символ
    return ''.join(ans)


print(easy_rle(target_string))
# ABCXYZDEFAB


def rle(s: str) -> str:
    def pack(s: str, cnt: int) -> str:
        if cnt > 1:  # если буква > 1 раза возвращает строку вида 'A4'
            return s + str(cnt)
        return s  # или просто букву

    last_symbol = s[0]
    last_pos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != last_symbol:
            # упаковывает последний символ и количество
            ans.append(pack(last_symbol, i - last_pos))
            last_pos = i  # обновляем последнюю позицию для нового символа
            last_symbol = s[i]  # обновляем символ
    ans.append(pack(s[last_pos], len(s) - last_pos))  # последний символ
    return ''.join(ans)


print(rle(target_string))
# A4B3C2XYZD4E3F3A6B12
