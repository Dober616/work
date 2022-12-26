import os

# folder_name = 'project'
# file_name = 'my_file.txt'
#
# way = 'my_docs|{folder}|{file}'.format(
#     folder=folder_name,
#     file=file_name
# )
#
# print(way)
#
#
# good_way = os.path.join('docs', folder_name, file_name)
# print(good_way)
#
#
# absolute_way = os.path.abspath(file_name)
# print(absolute_way)

def print_dirs(some_project):
    print(f'Содержание директории {some_project}')
    if os.path.exists(some_project):

        for element in os.listdir(some_project):
            way = os.path.join(project, element)
            print(way)
    else:
        print(f'каталога {some_project} не существует')



projects_list = ['Nothing_dir', 'work', 'repeat']
for project in projects_list:
    way_to_project = os.path.abspath(os.path.join('..', '..', '..', project))
    print_dirs(way_to_project)