

first_list = [1, 2, 3]
sec_list = [4, 6, 3, 2, 1]
first_list.extend(sec_list)
print(first_list)

for i in range(1, len(first_list)):

    first_list.remove(first_list[-i])
    print(first_list)

print('Новый список с уникальными эелементами:', first_list)

#
# list = ['a','b','c','c', 'd','e']
# list.remove('c')
# print(list)