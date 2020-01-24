#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input("Введите любое предложение: ")
user_list = user_string.split(' ')
for i, element in enumerate(user_list, 1):
    if len(element) > 10:
        element = element[0:10]
    print(f"{i}. - {element}")