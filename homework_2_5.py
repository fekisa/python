'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

'''
вариант 1
не соблюдено условие: натуральные числа + элемент размещается после существующих

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")

while True:
    number = int(input("Введите число: "))
    for i in range(len(my_list)):
        if my_list[i] == number:
            my_list.insert(i + 1, number)
            break
        elif my_list[0] < number:
            my_list.insert(0, number)
        elif my_list[-1] > number:
            my_list.append(number)
        elif my_list[i] > number and my_list[i+1] < number:
            my_list.insert(i+1, number)
            break
    print(f"Обновленный рейтинг - {my_list}")
'''

#вариант 2 (корректный)
rating_list = [22, 6, 5]
while True:
    user_input = input("Введите целое число или q для выхода\n")

    try:
        new_rating = abs(int(user_input))
    except ValueError as error:
        if user_input.lower() == "q":
            print("До свидания")
            break
        print("Ошибка ввода команды")
        continue
    # смотрим сколько таких записей уже есть в списке рейтинга
    new_rating_count = rating_list.count(new_rating)
    # если таковой рейтинг еще не используется
    if not new_rating_count:
        # определяем можно ли сразу вставить в начало или в конец новый рейтинг
        if new_rating > rating_list[0]:
            rating_list.insert(0, new_rating)
        elif new_rating < rating_list[-1]:
            rating_list.append(new_rating)
        else:
        # в том случае если нужный рейтинг надо вставить куда-то внутри, обходим его циклом
            for idx, itm in enumerate(rating_list):
                if itm < new_rating:
                    rating_list.insert(idx, new_rating)
                    break
    else:
        end_idx = rating_list.index(new_rating) + new_rating_count
        rating_list.insert(end_idx, new_rating)
    print(rating_list)