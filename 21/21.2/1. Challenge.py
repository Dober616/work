def find_fact(numm):
    if numm == 1:
        return 1
    fact = numm * find_fact(numm - 1)
    return fact

numm = int(input('Введите число: '))
print(find_fact(numm))