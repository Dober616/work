def drop_number():
    number = count_number-1 - len(people_round)
    return number

people_count = 5#int(input('Количество человек: '))
count_number = 7#int(input('Какое число в считалке: '))
people_round = []
print('Значит выбывает каждый', count_number, '- й человек', '\n++++++++++++++++++++++++++++++++++++')
for i in range(1, people_count+1):
    people_round.append(i)
print(people_round)

number = drop_number()

while len(people_round) != 1:
    if number > len(people_round):
        number -= len(people_round)
    people_round.pop(number)

    print(people_round)



print(people_round)



