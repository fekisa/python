'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''

my_list = [15, 2, 3, 1, 7, 5, 4, 10]

# первая запись (моя)
my_result_list = []
for idx, itm in enumerate(my_list):
    if my_list[idx -1] < my_list[idx]:
        my_result_list.append(itm)
print(my_list)
print(my_result_list)

# вторая запись (нашла в google)
my_result_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_result_list}')