def change_values(some_list, numm):
    for i_index, i_value in enumerate(some_list):
        some_list[i_index] += 10
    numm += 100

my_list = [1, 2, 3]
my_numm = 10

change_values(my_list, my_numm)

print(my_list, my_numm)