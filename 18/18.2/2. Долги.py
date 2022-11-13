debtor_name = input('Имя должника: ')
debt_summ = input('Сумма долга: ')
my_message = '{0}! {0}, hello! How are you {0}? Where my {1} rubles? {0}!'.format(debtor_name, debt_summ)
for _ in range(5):
    print(my_message)