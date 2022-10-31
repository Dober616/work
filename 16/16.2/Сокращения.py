def personnel():
    for i in money_list:
        if i == 0:
            money_list.remove(i)
    return money_list
def max_bet():
    maximum = 0
    for i in personnel():
        if i > maximum:
            maximum = i
    return maximum
def min_bet():
    minimum = max_bet()
    for i in personnel():
        if i < minimum:
            minimum = i
    return minimum

money_list = []
office = int(input('Количество сторудников: '))
for i in range (office):
    print('Зарплата ', i+1, 'cотрудника: ', end='')
    money = int(input())
    money_list.append(money)

print('Осталось сотрудников: ', len(personnel()))
print('Зарплаты: ', personnel())
print('Максимальная зарплата: ', max_bet())
print('Минимальная зарплата: ', min_bet())