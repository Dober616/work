# import random
# def tuple_change(nums):
#     index_tuple = tuple([random.randint(0, 5) for _ in range(5)])
#     value_tuple = random.randint(100, 1000)
#     nums[index_tuple] = value_tuple
#     return nums, value_tuple
#
# my_nums = 1 ,2, 3, 4, 5
# temp_nums = list(my_nums)
# print(my_nums)
#
#
# new_nums, rnd_values = tuple_change(temp_nums)
# print(temp_nums, rnd_values)

import random
def change(nums):
    nums = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums[index] = value
    return nums, value

my_nums = 1, 2, 3, 4, 5
my_nums_list = my_nums[:]
new_nums, rand_val = change(my_nums_list)
print(new_nums, rand_val)
new_nums = change(new_nums)
new_nums_list = new_nums[:]
rand_val += change(new_nums_list)
print(new_nums, rand_val)








