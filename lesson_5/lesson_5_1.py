my_file = open('test.txt', 'w')
lines = []
while True:
    line = input("Напишите что-нибудь \n")
    my_file.write(line + '\n')
    lines.append(line)
    if not line:
        break
my_file.close()

my_file = open('test.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()
