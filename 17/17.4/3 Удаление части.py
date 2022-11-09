import random
n = int(input('Сколько чисел?: '))
numm_list = [random.randint(1,100) for _ in range(n)]
print(numm_list)
a = random.randint(0, n)
b = random.randint(a + 1, n)
print(a)
print(b)
new_list = numm_list[:a] + numm_list[b:]
print(new_list)
