monsters_count = int(input('Введите количество монстров: '))
mage_index = int(input('Номер мага в списке: '))
monsters_damage = []
for monster in range (monsters_count):
    print ('Урон ', monster+1,'монстра: ', end = ' ')
    damage = int(input())
    monsters_damage.append(damage)
print(monsters_damage)
for i in range (monsters_count):
    if monsters_damage[i] < 100 and i!=mage_index -1:
        monsters_damage[i] += monsters_damage[mage_index-1]

print(monsters_damage)