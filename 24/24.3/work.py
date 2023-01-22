class User:
    user_name = 'Admin'
    password = 'asdfg'
    is_banned = False
    friends = []

    def print_info(self):
        print(f'Имя пользователя: {self.user_name}'
              f'\nпароль: {self.password}'
              f'\nстатус бана: {self.is_banned}'
              f'\nдрузья: {self.friends}')

    def add_fritnd(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.user_name)
        else:
            self.friends.append(friend)


user_1 = User()
user_2 = User()
user_2.user_name = 'Алина'
user_1.add_fritnd('Bob')
user_1.add_fritnd(user_2)
user_1.print_info()