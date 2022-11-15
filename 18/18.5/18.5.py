details_count = 5000000000
price = 23.8589578
increase = 0.045678


print('На складе {:,d} деталей'.format(details_count))
print('На складе {:.0e} деталей'.format(details_count))
print('Каждая деталь стоит {:.2f} рублей'.format(price))
print('Цена увелиличилась на {:.1%}'.format(increase))