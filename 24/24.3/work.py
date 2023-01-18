class User:
    user_name = 'Admin'
    password = 'qwert'
    is_banned = False
    frends = []

    def print_info(self):
        print(
            f'Имя: {self.user_name};\n'
            f'пароль: {self.password};\n'
            f'статус: {self.is_banned};\n'
            f'друзья: {self.frends}'
        )
    def add_friend(self, friend):
        if isinstance(friend, User):
            self.frends.append(friend.user_name)
        else:
            self.frends.append(friend)

user_1 = User()
user_2 = User()
user_2.user_name = 'Алина'
user_1.add_friend('Bob')
user_1.add_friend('Egor')
user_1.add_friend(user_2)
user_1.print_info()