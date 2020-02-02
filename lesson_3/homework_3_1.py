'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def my_division (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Деление на ноль невозможно"
    except ValueError:
        return "Ошибка ввода. Введите число"

print(my_division(int(input("Введите x = ")), int(input("Введите y = "))))
