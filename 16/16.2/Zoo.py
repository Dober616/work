def removes():
    actions = input('Введите действие (добавить, переместить, удалить): ')
    if actions == 'добавить':
        animal = input('Кого добавляем? : ')
        place = input('Перед кем добавляем? : ')
        zoo.insert(zoo.index(place), animal)
    elif actions == 'переместить':
        animal = input('Кого перемещаем? : ')
        place = input('С кем меняем местами? : ')
        zoo.insert(zoo.index(place)+1, animal)
        zoo.remove(animal)
    elif actions == 'удалить':
        animal = input('Кого удаляем? : ')
        zoo.remove(animal)

    return zoo




zoo = ['leon', 'bear', 'elefant', 'monkey']

print('Зоопарк: ', removes())
print('Лев сидит в клетке номер ', zoo.index('leon')+1)
print('Обезьяна сидит в клетке номер ', zoo.index('monkey')+1)
