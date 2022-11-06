team_list = []
numm = 1
members = int(input('Количество участников всего: '))
team = int(input('Количество участников в команде: '))
for _ in range(members // team):
    team_list.append(list(range(numm, numm + team)))
    numm += team
print(team_list)
