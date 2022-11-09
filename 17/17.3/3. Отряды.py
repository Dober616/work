import random
frst_squad = [random.randint(50, 80) for _ in range(10)]
sec_squad = [random.randint(30, 60) for _ in range(10)]

thrd_squad = [('Погиб' if frst_squad[damage] + sec_squad[damage] > 100 else 'Выжил') for damage in range(10)]
print(frst_squad)
print(sec_squad)
print(thrd_squad)
