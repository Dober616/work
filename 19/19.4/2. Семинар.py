import random

def set_lists(nums):
    new = set(nums)
    new.discard(min(nums))
    new.add(random.randint(100, 200))
    return new
nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

print(set_lists(nums_1))
print(set_lists(nums_2))
print('Объединение множеств: ', set_lists(nums_1).union(set_lists(nums_2)))
print('Пересечение множеств: ', set_lists(nums_1).intersection(set_lists(nums_2)) )
print('Элементы, входящие в nums_2, но не входящие в nums_1: ', set_lists(nums_1).difference(set_lists(nums_2)))