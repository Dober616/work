# def from_string(cls, date_as_string):
#     day, month, year = map(int, date_as_string.split('-'))
#     date = cls(day, month, year)
from typing import List

my_nums: List[int] = [3, 1, 4, 1, 5, 9, 2, 6, 2]
other_nums: List[int] = [2, 7, 1, 8, 2, 8, 1, 8, 100]

result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))
print(result)

print(list(map(lambda x, y: 1, [1, 2], [2, 3, 4])))

# animals = ['cat', 'dog', 'cow']
# result = list(map(lambda x: x.capitalize(), animals))
# print(result)

some_result = list(filter(lambda x: x % 2 == 0, result))
print(some_result)