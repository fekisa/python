'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
'''

def my_func(x,y):
        if x < 0 or y > 0:
            print("Данные не соответствуют условиям. x - действительное положительное число, y - целое отрицательно число")
        elif x == 0 or y == 0:
            print("Тут не понятно, кто прав")
        else:
            print(x**y)

my_func(int(input("Введите x: ")), int(input("Введите y: ")))