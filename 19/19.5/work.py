data = [
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'},
    {'id': 12, 'user': 'Anton'},
    {'id': 10, 'user': 'Bob'},
    {'id': 11, 'user': 'Misha'}
]
unique_data = []
# for i in data:
#     if i in unique_data:
#         pass
#     else:
#         unique_data.append(i)

unique_data_dict = {user['id']: user for user in data}
print(unique_data_dict.values())
print(data)