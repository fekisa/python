'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

#решение через list. Вариант 1
'''
month_number = int(input("Введите номер месяца: "))
seasons_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if month_number in seasons_list[0:2]:
    print("Зима")
elif month_number in seasons_list[3:5]:
    print("Весна")
elif month_number in seasons_list[6:8]:
    print("Лето")
elif month_number in seasons_list[9:11]:
    print("Осень")
else:
    print("Число введено неверно. Интервал от 1 до 12")
'''

#решение через list. Вариант 2. Оптимальный
seasons_list = ["Зима",
                "Весна",
                "Лето",
                "Осень",
                ]
while True:
    user_month_num = input("Введите номер месяца: ")
    try:
        #пробуем преобразовать к числу
        user_month_num = int(user_month_num)
        #проверяем что это число может быть номером месяца
        if 12 < user_month_num or user_month_num < 0:
            print("f'Ошибка ввода: номер месяца не может быть больше 12")
            continue
    except ValueError as e:
        print(f'Ошибка ввода необходимо ввести число (номер месяца)')
        print(e)
        continue
    # вычисляем индекс времени года
    season_idx = user_month_num // 3 % 4
    #берем из списка индекс времени года
    print(seasons_list[season_idx])
    break

#решение через dict.
month_number = int(input("Введите номер месяца: "))
seasons = {'Зима': (12, 1, 2),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
for key in seasons.keys():
    if month_number in seasons[key]:
        print(key)