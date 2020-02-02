'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

# Мой вариант решения

def user_info(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)

user_info(name = "Anna", surname = "Chernyshenko", year = 1988, city = "Moscow", email = "email@gmail.com", phone = "123")

# Вариант наставника // проверить позже и добавить

def user_data(name: str, surname: str, birth_year: int, city: str, email: str, phone: int):
    '''
    Отображает данные о пользователе
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: None
    '''
    return f"{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone}"

# ИЛИ

def user_data_kw(**kwargs) -> str:
    '''
    Отображает данные о пользователе
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: str
    '''

    name = kwargs.get('name') or ''
    surname = kwargs.get('surname') or ''
    birth_year = kwargs.get('birth_year') or ''
    city = kwargs.get('city') or ''
    email = kwargs.get('email') or ''
    phone = kwargs.get('phine') or ''
    return f"{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone}"