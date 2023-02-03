# def counter():
#     n = 0
#     while True:
#         n += 1
#         yield n
#         if n == 100:
#             return
#
# for i in counter():
#     print(i, end=' ')

def get_prime(last_numm):
    for number in range(2, last_numm + 1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number

for i in get_prime(100):
    print(i, end=' ')

