import  random
class RandomNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return random.randint(0, 10)
        else:
            raise StopIteration('Достигнут установленный лимит')


my_iter = RandomNumbers(3)

for i in my_iter:
    print(i)
