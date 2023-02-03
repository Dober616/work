def fibonacci(number):
    cur_value = 0
    next_value = 1
    for _ in range(number):
        yield cur_value
        cur_value, next_value = next_value, cur_value + next_value
        if cur_value > 10 ** 6:
            return

def square(nums):
    for num in nums:
        yield num ** 2

my_fib = fibonacci(10000000000)
for i in my_fib:
    print(i, end=' ')

print('\n')
print(sum(square(fibonacci(5000))))
print()
cubes_gen = [num **3 for num in range(10)]
for i in cubes_gen:
    print(i, end=' ')