import os
import random


def find_my_file(current_way, file_name):
    all_ways = []
    for element in os.listdir(current_way):
        way = os.path.join(current_way, element)
        if file_name == element:
            all_ways.append(os.path.abspath(way))
        elif os.path.isdir(way):
            result = find_my_file(way, file_name)
            if result:
                all_ways.extend(result)
    return all_ways

def check_file_inside(way_to_file):
    file = open(way_to_file, 'r')
    for line in file:
        print(line)
    file.close()

all_ways = find_my_file('..', 'group_1.txt')
check_file_inside(random.choice(all_ways))