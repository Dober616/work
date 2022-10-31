def exist_list(film_list):
    for i in film_list:
        if i == film:
            return True
    return False
film_list = ['Во все тяжкие', 'Клиника', 'Друзья', 'Интерны', 'Королева юга', 'Химера', 'Игры престолов',
             'Офис', 'Все ненавидят криса', 'Полицейский с рублевки', 'Лост', 'Универ']
my_list = []
while True:
    print ('Рейтинг фильмов: ', my_list)
    film = input('Введите название фильма: ')
    if exist_list(film_list):
        print('Выберите действие (добавить, удалить, вставить): ', end='')
        action = input()
        if action == 'добавить':
            if exist_list(my_list):
                print('Такой фильм уже есть в вашем списке')
            else:
                my_list.append(film)
        elif action == 'удалить':
            my_list.remove(film)
        elif action == 'вставить':
            if exist_list(my_list):
                print('Такой фильм уже есть в вашем списке')
            else:
                paste = input('Перед каким фильмом вставляем? ')
                my_list.insert(my_list.index(paste),film)
    else:
        print('Такого фильма нет. Что будем делать (добавить, вставить)? ', end = '')
        action = input()
        if action == 'добавить':
            if exist_list(my_list):
                print('Такой фильм уже есть в вашем списке')
            else:
                my_list.append(film)
        elif action == 'вставить':
            if exist_list(my_list):
                print('Такой фильм уже есть.')
            else:
                paste = input('Перед каким фильмом вставляем? ')
                my_list.insert(my_list.index(paste),film)
