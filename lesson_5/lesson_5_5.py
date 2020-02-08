my_file = open('test_5.txt', 'w')
lines = input("Введите последовательность чисел через пробел \n")
my_file.write(lines)
number = lines.split(" ")
my_file.close()

my_file = open('test_5.txt', 'r')
print(sum(map(int, number)))
my_file.close()