def get_price():
    price = float(input('Цена на товар: '))
    return price
price_list = [get_price() for i in range(5)]
print(price_list)
first_promotion = int(input('Первое повышение: '))
second_promotion = int(input('Второе повышение: '))
first_promotion_list = [price + price * first_promotion / 100 for price in price_list]
second_promotion_list = [price + price * second_promotion / 100 for price in first_promotion_list]

print('Сумма цен за каждый год: ',round(sum(price_list), 2), round(sum(first_promotion_list), 2), round(sum(second_promotion_list), 2))
