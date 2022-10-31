def is_film_exist(movie, films):
    for i_movie in films:
        if i_movie == movie:
            return True
    return False
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо']

my_list = []
while True:
    print('\nВаш текущий топ фильмов: ', my_list)
    new_movie = input('Название фильма: ')
    if is_film_exist(new_movie, films):
        print('Конанды: добавить, удалить, вставить')
        command = input('Введите команду: ')
        if command == 'добавить':
            my_list.append(new_movie)
        elif command == 'удалить':
            if is_film_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print('Такого фильма нет в нашем рейтинге.')
        elif command == 'вставить':
            place = int(input('На какое место вставить фильм: '))
            my_list.insert(place-1, new_movie)

    else:
        print('Такого фильма нет на сайте')
