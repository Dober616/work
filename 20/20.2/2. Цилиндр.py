import math
def cilinder_square():
    side = 2 * math.pi * radius * height
    cicle_square = math.pi * (radius ** 2)
    return side, cicle_square


height = int(input('Высота цилиндра: '))
radius = int(input('Радиус цилиндра: '))

full = cilinder_square()[0] + 2 * cilinder_square()[1]
print(f'Площадь цилиндра {round(full, 2)}')