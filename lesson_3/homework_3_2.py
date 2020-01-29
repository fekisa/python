'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def user_info(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)

user_info(name = "Anna", surname = "Chernyshenko", year = 1988, city = "Moscow", email = "email@gmail.com", phone = "123")
