pack = []
decode = []
bad_packs = 0
packs_amt = int(input('Количество пакетов: '))
for i_pack_num in range(packs_amt):
    print('\nПакте номер', i_pack_num + 1)
    for i_bit in range (4):
        print(i_bit + 1, 'бит: ', end=' ')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете')
        bad_packs += 1
    pack = []

print('\nПолученное сообщение: ', decode)
print('Количество ошибок в сообщении: ', decode.count(-1))
print('Количество потерянных пакетов: ', bad_packs)