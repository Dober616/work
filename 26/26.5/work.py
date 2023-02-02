def fibonacci(number):

    curent_value = 0
    next_value = 1
    for _ in range(number):
        yield curent_value
        curent_value, next_value = next_value, curent_value + next_value
        if curent_value > 10 ** 6:
            return

def square(nums):
    for num in nums:
        yield num ** 2


fib = fibonacci(100000)
for i in fib:
    print(i, end=' ')
print('\n')
print(sum(square(fibonacci(5000))))

print()
cubes_gen = (i ** 3 for i in range(10))
for i in cubes_gen:
    print(i)