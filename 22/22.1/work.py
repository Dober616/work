import os

# my_folder = 'project'
# my_file = 'my_file.txt'
#
# way = f'docs/{my_folder}/{my_file}'
#
# os_way = os.path.join('docs', my_folder, my_file)
#
# print(way)
# print(os_way)
#
# abs_way = os.path.abspath(my_file)
# print(abs_way)
def dir_content(folder):
    for elememt in os.listdir(folder):
        path_to_element = os.path.join(folder, elememt)
        print(path_to_element)


folder_name = '22'
path_to_folder = os.path.abspath(os.path.join('..', '..', folder_name))
dir_content(path_to_folder)