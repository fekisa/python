#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

#Решение №1
user_number = int(input("Введите число: "))
m = user_number % 10
user_number = user_number//10
while user_number > 0:
    if user_number % 10 > m:
        m = user_number % 10
    user_number = user_number//10
print(m)

#Решение №2
user_number = input("Введите число: ")
print(max(user_number))

#Решение №3
user_number = input("Введите число: ")
x = 0
for i in user_number:
    while int(i) > x:
        x = int(i)
print(x)