'''
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]
#Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
#Пример:
#{
#“название”: [“компьютер”, “принтер”, “сканер”],
#“цена”: [20000, 6000, 2000],
#“количество”: [5, 2, 7],
#“ед”: [“шт.”]
#}
'''

'''
Вариант 1
goods = []
features = {'name': '', 'price': '', 'quantity': ''}
analytics = {'name': [], 'price': [], 'quantity': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
'''

# Вариант 2 (корректный)
# шаблон товара сразу с вопросом к пользователю и типом ожидаемых данных
product_template = {
    "название": ("имя товара", str),
    "цена": ("стоимость товара", int),
    "количество": ("количество товара", int),
    "ед": ("единицы измерения (шт., кг и т.д)", str),
}

#флаг для понимания надо нам еще товар добавлять в список или нет
next_enter = True

#автоинкримент для номера товара
auto_inc = 1

#список для хранения наших товаров
product_list = []

while next_enter:
    #словарь в который мы будем запонять атрибуты товара
    product = {}
    #заполняем товар по шаблону
    for key, value in product_template.items():
        #цикл while True я использую для того чтобы переспросить вопрос если будет неверный ввод по типу
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f"{e}\n Не верное значение данных")
                continue
            product[key] = user_value
            break
    product_list.append((auto_inc, product))
    auto_inc += 1

    #тут мы проверим надо еще товар вводить или нет
    while True:
        next_add = input("Добавить еще продукт? Да / Нет\n")
        if next_add.lower() in ("да", "нет"):
            next_enter = next_add.lower() == "да"
            break
        else:
            print("Неверный ввод, повторите")
product_analytics = {}

#собираем словарь аналитики
for key in product_template:
    product_analytics[key] = [itm[1][key] for itm in product_list]

#собираем словарь аналитики
product_analytics = {key: [itm[1][key] for itm in product_list ] for key in product_template}

print(1)
print(product_list)
print(product_analytics)