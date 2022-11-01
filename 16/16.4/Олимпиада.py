N = int(input('Количество участников: '))
members = []
numm = 1
for _ in range(N // 3):
    members.append(list(range(numm,numm + 3)))
    numm += 3
print(members)