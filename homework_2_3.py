#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_number = int(input("Введите номер месяца: "))

#решение через list
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

#решение через dict
seasons = {'Зима': (12, 1, 2),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
for key in seasons.keys():
    if month_number in seasons[key]:
        print(key)