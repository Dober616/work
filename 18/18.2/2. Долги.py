# debtor_name = input('Имя должника: ')
# debt_summ = input('Сумма долга: ')
# my_message = '{0}! {0}, hello! How are you {0}? Where my {1} rubles? {0}!'.format(debtor_name, debt_summ)
# for _ in range(5):
#     print(my_message)

debtor_name = input('Введите имя должника: ')
summ_debt = input('Введите сумму долга: ')
message = '{name}! Привет {name}! Как дела, {name}? Где мои {summ} рублей? {summ} рублей {name}!!!'.format(name=debtor_name, summ=summ_debt)
print(message)