#Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

#1 способ // input список только для чисел
#n = int(input("Введите длину списка: "))
#for i in range(0, n):
#    print("Введите значение №", i, ":")
#    item = int(input())
#    my_list.append(item)
#print(my_list)

#2 способ // универсальный
input_string = input("Введите элементы списка, разделяя их пробелом: ")
my_list = input_string.split()
print(my_list)
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(' '.join([str(i) for i in my_list]))