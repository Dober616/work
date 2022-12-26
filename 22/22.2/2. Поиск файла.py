import os


def find_file_name(my_way, name):
    for element in os.listdir(my_way):
        way = os.path.join(my_way, element)
        if name == element:
            print(os.path.abspath(way))
        elif os.path.isdir(way):
            result = find_file_name(way, name)
            if result:
                break
    else:
        result = None
    return result


file_name = 'work.py'

find_file_name('..', file_name)
