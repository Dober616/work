import random

class Car:
    color = 'Red'
    price = 1000000
    max_speed = 200
    current_speed = 0


toyota = Car()
mazda = Car()
bmw = Car()
toyota.max_speed = random.randint(1, 200)
mazda.max_speed = random.randint(1, 200)
bmw.max_speed = random.randint(1, 200)
print(toyota.max_speed)
print(mazda.max_speed)
print(bmw.max_speed)
