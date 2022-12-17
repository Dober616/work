def change_values(some_list):
    for i_index, i_value in enumerate(some_list):
        some_list[i_index] += 3


my_list = [10, 20, 30]
number = 100
change_values(my_list)
print(my_list)
