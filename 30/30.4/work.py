# def from_string(cls, date_as_string):
#     day, month, year = map(int, date_as_string.split('-'))
#     date = cls(day, month, year)

my_nums = [3, 2, 5, 1, 5, 6]
other_nums = [3, 5, 2, 6, 8, 4]

new_list = map(lambda a, b: a + b, my_nums, other_nums)
print(list(new_list))