'''
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count
from itertools import cycle

for el in count(int(input('Введите стартовое число '))):
    print(el) # беконечный цикл

my_list = [1, 'abc', 123, 'hello']
for el in cycle(my_list):
    print(el) # беконечный цикл