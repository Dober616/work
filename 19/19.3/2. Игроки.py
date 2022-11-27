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


teammate_a = [player['name'] for player in players_dict.values() if player['team'] == 'A' and player['status'] == 'Rest']
print(teammate_a)
teammate_b = [player['name'] for player in players_dict.values() if player['team'] == 'B' and player['status'] == 'Training']
print(teammate_b)
teammate_c = [player['name'] for player in players_dict.values() if player['team'] == 'C' and player['status'] == 'Travel']
print(teammate_c)