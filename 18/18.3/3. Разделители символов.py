congratulations = 'С днем рожденья тебя, {name}! С {age}-летием тебя!'
names_list = input('Введите имя: ').split(', ')
ages_list = input('Введите возраст: ').split()

print(names_list)
print(ages_list)
for i in range(len(names_list)):
    print(congratulations.format(name=names_list[i], age=ages_list[i]))

congrat_list = ['-'.join([names_list[i], ages_list[i]]) for i in range(len(names_list))]
print('Именинники: ', end='')
print(congrat_list)