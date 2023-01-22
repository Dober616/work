class Potato:
    def __init__(self, index):
        self.index = index
        self.state = 0



class Garden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]
