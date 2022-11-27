import random

numbers_list = [random.randint(1,4) for _ in range(10)]
# print(numbers_list)
# new_list = []
# for number in numbers_list:
#     if number not in new_list:
#         new_list.append(number)
# print(new_list)

unique = set(numbers_list)
print(unique)