names_file = open('my_names.txt', 'w')
for _ in range(5):
    name = input('Введите имя сотрудника: ')
    names_file.write(name)
names_file.close()
names_file = open('my_names.txt', 'r')
result = 0
for line in names_file:
    result += len(line.rstrip())
    if len(line.rstrip()) < 3:
        raise Exception
print(result)
