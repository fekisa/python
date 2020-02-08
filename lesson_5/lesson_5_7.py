"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import statistics
import json

db_file = '/Users/fekisa/GIT/geekbrains/phyton/lesson_5/test_7.txt'

result_file = '/Users/fekisa/GIT/geekbrains/phyton/lesson_5/test_7_result.json'

firms = dict()


with open(db_file, 'r') as file:
    for line in file:
        tmp = line.split(' ')
        name = tmp[0]
        a, b = int(tmp[2]), int(tmp[3])
        firms[name] = a - b

result = []
result.append(firms)
result.append({'average_profit': statistics.mean([itm for itm in firms.values() if itm >= 0])})

with open(result_file, 'w') as file:
    file.write(json.dumps(result))
