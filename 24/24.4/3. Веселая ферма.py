class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Спелая'}
    def __init__(self, index):
        self.index = index
        self.states = 0

    def grow(self):
        if self.states < 3:
            self.states += 1
        self.print_state()


    def is_ripe(self):
        if self.states == 3:
            return True

    def print_state(self):
        print(f'картошка {self.index} сейчас {Potato.states[self.states]}')




class Garden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all(potato.is_ripe() for potato in self.potatoes):
            print('Картошка еще не созрела')
            return False
        else:
            print('Вся картошка созрела')
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()

garden = Garden(5)
for _ in range(3):
    garden.grow_all()
garden.are_all_ripe()