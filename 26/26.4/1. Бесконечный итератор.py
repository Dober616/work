class Iterator:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return self.count

my_iterator = Iterator()
for i in my_iterator:
    print(i)
