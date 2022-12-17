def quit_application(question, warning = 'Да определись ты блять уже', attemps = 3):
    while True:
        answer = input(question).lower()
        if answer == 'да':
            return True
        elif answer == 'нет':
            return None
        else:
            print(warning)
        attemps -= 1
        if attemps == 0:
            print('Попытки закончились, идите нахуй')
            break


exit_app = quit_application('Вы действительно хотите выйти? ')
if exit_app:
    close_file = quit_application('Закрыть файл? ')
    save_file = quit_application('Сохранить ваш файл? ')
