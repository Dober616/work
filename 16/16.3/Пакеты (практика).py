summ_pack = []
pack = []
mistakes = 0
lost_packs = 0
pack_count = int(input('Количество пактетов: '))
for i in range(pack_count):
    print('Введите пакет №', i+1)
    for i in range (4):
        print(i+1, 'бит: ', end='')
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) == 0:
        summ_pack.extend(pack)
    elif pack.count(-1) == 1:
        summ_pack.extend(pack)
        mistakes += 1
    else:
        print('Много ошибок в пакете')
        lost_packs += 1
        mistakes += 1

print('Полученное сообщение: ', summ_pack)
print('Количество ошибок в сообщении: ', mistakes)
print('Количество потерянных пакетов: ', lost_packs)
