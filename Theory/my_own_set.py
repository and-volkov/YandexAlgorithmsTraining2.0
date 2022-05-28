"""Написать свое собственное множество"""

"""
F(x) = X % setsize - хеш-функция
MySet (список списков) - хеш-таблица
Совпадения значений хещ-функции для разных параметров - коллизия
"""


class MySet:
    def __init__(self, setsize):
        self.setsize = setsize
        self.my_set = [[] for _ in range(self.setsize)]

    def add(self, x):
        if not self.find(x):  # если такого элемента нет - добавляем
            self.my_set[x % self.setsize].append(x)

    def find(self, x):
        for item in self.my_set[x % self.setsize]:
            if item == x:
                return True
        return False

    def delete(self, x):
        xlist = self.my_set[x % self.setsize]
        for i in range(len(xlist)):
            if xlist[i] == x:
                xlist[i] = xlist[len(xlist) - 1]
                xlist.pop()
                return

    def __str__(self):
        return str(self.my_set)


test_set = MySet(10)
print(test_set)
# [[], [], [], [], [], [], [], [], [], []]
test_set.add(10)
test_set.add(99)
print(test_set)
# [[10], [], [], [], [], [], [], [], [], [99]]
print(test_set.find(10))
# True
print(test_set.find(11))
# False
test_set.delete(10)
print(test_set)
# [[], [], [], [], [], [], [], [], [], [99]]
