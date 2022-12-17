def tax_doc(tax, *args, **kwargs):
    price_summ = 0
    for i_price in args:
        price_summ = price_summ + i_price * tax / 100
    print(f'Сумма цен с учетом налога: {price_summ}')
    for i_data, i_value in kwargs.items():
        print(f'{i_data}: {i_value}')





tax = int(input('Величина налога: '))
tax_doc(tax, 1000, 950, 820, 990, 987,
        year=1997, doctype='report', operation_id=11133388)