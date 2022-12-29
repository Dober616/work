import os

file_1 = open('/Users/kirilldruzak/PycharmProjects/task/group_1.txt', 'r')
file_2 = open('/Users/kirilldruzak/PycharmProjects/task/group_2.txt', 'r')
point_summ = 0
point_diff = 0
point_multiple = 1
for i_line in file_1:
    info = i_line.split()
    point_summ += int(info[2])
    point_diff -= int(info[2])


for i_line in file_2:
    info = i_line.split()
    point_multiple *= int(info[2])


print(f'Сумма очков 1 команды: {point_summ}\nРазность очков 1 команды: {point_diff}\nПроизведение очков 2 команды: {point_multiple}')
