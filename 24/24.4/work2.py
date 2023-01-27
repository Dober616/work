class Potato:
    states = {
        0: 'Отсутствует',
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
        self.print_state()

    def print_state(self):
        print(f'Картошка {self.index} в стадии {Potato.states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False

class Potato_garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        for potato in self.potatoes:
            if not potato.is_ripe():
                print('Картошка еще не созрела')
        else:
            print('Вся картошка созрела, можно собирать')

my_garden = Potato_garden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
