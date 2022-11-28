# {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "ssh": {
#             "access": "true",
#             "login": "ivan",
#             "password": "qwerty"
#         }
#     }
# }

# data = dict()
# #  до этого что-то происходит
# print(data.get('server'))
# data['server'] = {
#     'host': '127.0.0.1',
#     'port': '10'
# }
# # еще что-то происходит
# if data.get('configuration', {}).get('ssh', {}).get('login', {}):
#     print('В структуре уже есть логин')
# print(data.get('configuration', {}).get('ssh', {}).get('login', {}))
# data['configuration'] = {
#     'ssh': {
#         'access': 'true',
#         'login': 'Ivan',
#         'password': 'qwerty'
#     }
# }
# print(data)


players_dict = {
1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
5: {'name': 'Andrey', 'team': 'A', 'status': 'Training'},
6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'},
}

# team_a = [
#     player['name']
#     for player in players_dict.values()
#     if player['team'] == 'A' and player['status'] == 'Rest'
# ]
# print(team_a)
