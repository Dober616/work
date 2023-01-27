class User:
    user_name = 'Admin'
    password = 'qwert'
    is_banned = False
    friends = []

    def info(self):
        print(f'Имя пользователя: {self.user_name}'
              f'\nПароль: {self.password}'
              f'\nСтатус: {self.is_banned}'
              f'\nДрузья: {self.friends}')

    def add_friend(self, friend_name):
        if isinstance(friend_name, User):
            self.friends.append(friend_name.user_name)
        else:
            self.friends.append(friend_name)


user_1 = User()
user_2 = User()
user_2.user_name = 'Алина'
user_1.add_friend('Егор')
user_1.add_friend('Сергей')
user_1.add_friend(user_2.user_name)
user_1.info()

