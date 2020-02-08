my_file = open('test_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(f'Количество символов {i + 1}-ой строки {len(content[i])-1}')
my_file.close()