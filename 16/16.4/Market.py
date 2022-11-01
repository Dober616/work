goods = [['apples', 50], ['oranges', 190], ['peaches', 200], ['bananas', 130]]

new_fruit = input('Новый фрукт: ')
price = int(input('Цена нового фрукта: '))
new_list = []
new_list.append(new_fruit)
new_list.append(price)
goods.append(new_list)
print('Новый ассортимент: ', goods)
for i in goods:
    i[1] += i[1] * 8 / 100
print('Новый ассортимент с увеличенной ценой: ', goods)