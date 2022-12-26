def print_tax_doc(tax, *args, **kwargs):
    price_sum = 0
    for i in args:
        price_sum = price_sum + i * tax / 100
    print(f'Сумма цен с учетом налога: {price_sum}')
    for i, y in kwargs.items():
        print(f'{i}: {y}')


my_tax = int(input('Величина налога: '))
print_tax_doc(my_tax, 1000, 950, 880, 920, 990, year=2022, day='friday', doc_num=12345678)