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

team_a_rest = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]

team_b_training = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]
team_c_travel = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]
print(team_a_rest)
print(team_b_training)
print(team_c_travel)
print(players_dict)