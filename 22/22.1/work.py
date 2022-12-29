import os

#
# folder_name = 'project'
# file_name = 'my_file.txt'
#
# way = 'docs|{folder}|{file}'.format(
#     folder=folder_name,
#     file=file_name
# )
#
# print(way)
#
# my_way = os.path.join('documents', folder_name, file_name)
# print(my_way)
#
# abs_way = os.path.abspath(file_name)
# print(abs_way)
def print_directories(my_project):
    print(f'Содержимое директории {my_project}')
    for element in sorted(os.listdir(my_project)):
        print(element)
        # way = os.path.join(my_project, element)
        # print(f'         {way}')


project_list = ['work', 'dpo_python_basic']

for project in project_list:
    way_to_project = os.path.abspath(os.path.join('..', '..', '..', project))
    print_directories(way_to_project)