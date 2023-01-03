import os


def find_file(current_path, file_name):
    path_list = []
    for element in os.listdir(current_path):
        path = os.path.join(current_path, element)
        if element == file_name:
            path_list.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    return path_list


def get_from(my_file_path):
    file = open(my_file_path, 'r')
    result = ''
    for line in file:
        result += line
    return result


my_files = find_file('/Users/druz_kirill/PycharmProjects/', 'work.py')
my_result = open('scripts.txt', 'w')

for file_path in my_files:
    my_result.write(get_from(file_path))
    my_result.write('\n' + "*" * 40)
my_result.close()