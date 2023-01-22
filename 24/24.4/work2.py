class Potato:

    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Спелая'}
    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка растет!')
        for some_potato in self.potatoes:
            some_potato.grow()

    def are_all_right(self):
        for some_potato in self.potatoes:
            if not some_potato.is_ripe():
                print('Картошка еще не созрела')
                self.grow_all()
                break
            else:
                print('Вся картошка созрела, можно собирать')


my_garden = Garden(5)
for _ in range(3):
    my_garden.are_all_right()