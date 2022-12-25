import copy
import random

def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {
    1: 'text',
    2: 'another_text'
}
uniq_nums = {1, 2, 3}
common_dict = {
    1: nums_list,
    2: some_dict,
    3: uniq_nums,
    4: (10, 20, 30)
}
common_dict_copy = copy.deepcopy(common_dict)
change_dict(common_dict_copy)
for i in common_dict_copy:
    print(common_dict_copy[i])

print(f'{nums_list}\n {some_dict}\n {uniq_nums}')

