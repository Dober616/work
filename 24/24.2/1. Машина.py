import random

class Some_car:
    color = 'color'
    price = 'some_price'
    max_speed = 'speed'
    current_speed = 0

toyota = Some_car()
toyota.color = 'red'
toyota.price = 2000000
toyota.max_speed = random.randint(0, 100)

print(toyota.color, toyota.price, toyota.max_speed)