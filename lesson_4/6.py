'''
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
'''
from itertools import count, cycle

# ACHTUNG - беконечный цикл 1!

# for el in count(int(input('Введите стартовое число '))):
#     print(el)

# ACHTUNG - беконечный цикл 2!

i = 0

list = [el for el in range(0, i)]
print(list)

list =["ABC", True, 4**i,[1, 2, 3, 4]] # 4**i всегда равен 1
for someting in cycle(list):
    i += 1
    print(someting)