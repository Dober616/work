# speakers_file = open('speakers.txt', 'r')
# sym_count = []
#
# for line in speakers_file:
#     print(line, end='')
#     sym_count.append(str(len(line)))
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
#
#
# counts_file = open('symbol_counts.txt', 'w')
# counts_file.write(sym_count_str)
# counts_file.write('\nhuy')
# counts_file.close()


import os

def find_file(cur_path, file_name):
    print('переходим', cur_path)

    for element in os.listdir(cur_path):
        path = os.path.join(cur_path, element)
        print(f'    смотрим {path}')

        if file_name == element:
            return path
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None
    return result

file_path = find_file(os.path.abspath(os.path.join('..', '..', '..', 'Work')), 'try.py')
history_file = open('search_history.txt', 'a')

if file_path:
    print('Абсолютный путь к файлу: ', file_path)
    history_file.write(file_path)
else:
    print('Файл не найден')
history_file.close()