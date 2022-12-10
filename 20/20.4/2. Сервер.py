server_data = {
    'server': {
        'host': '127.0.0.1',
        'port': '10'
    },
    'configuration': {
        'access': 'true',
        'login': 'ivan',
        'password': 'qwerty'
    }
}
for title, data in server_data.items():
    print(f'{title}:')
    for i, y in data.items():
        print(f'\t{i}: {y}')