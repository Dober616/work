incomes = {
    'apple':5600.20,
    'orange':3500.45,
    'banana':5000.00,
    'grapefruit':300.40,
    'bergamot':3700.56,
    'durian':5987.23,
    'peach':10000.50,
    'persimmon':310.00
}


min_value = 0
min_name = ''
for name, value in incomes.items():
    if min(incomes.values()) == value:
        min_value = value
        min_name = name


print('Общий доход за год составил: ', sum(incomes.values()), 'рублей.')
print('Самый маленький доход за год принес {0}.'.format(min_name), 'Он составляет{0} рублей.'.format(min(incomes.values())))
incomes.pop(min_name)
print(sorted((incomes.values()), reverse=True))
print(incomes)
