class Potato:

    states = {0: 'Отсутствует',
              1: 'Росток',
              2: 'Зеленая',
              3: 'Зрелая'
              }


    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.state_info()


    def is_ripe(self):
        if self.state == 3:
            return True



    def state_info(self):
        print(f'Картошка {self.index} сейчас в стадии: {Potato.states[self.state]}')


class Potato_garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка растет!')
        for my_potato in self.potatoes:
            my_potato.grow()

    def are_all_right(self):
        if not all([my_potato.is_ripe() for my_potato in self.potatoes]):
            print('Картошка еще не зозрела')
        else:
            print('Вся картошка уже созрела, можно собирать!')


my_garden = Potato_garden(5)
my_garden.are_all_right()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_right()