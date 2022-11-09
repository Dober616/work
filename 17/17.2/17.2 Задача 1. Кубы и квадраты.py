left_board = int(input('Левая граница: '))
right_board = int(input('Правая граница: '))

numm_cubes = [number ** 3 for number in range(left_board, right_board + 1)]
numm_squares = [number ** 2 for number in range(left_board, right_board + 1)]
print(numm_cubes)
print(numm_squares)