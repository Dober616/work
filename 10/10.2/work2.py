for row in range(20):
    for col in range(50):
        if col == 24:
            print('/', end='')
        elif row == 9:
            print('-', end='')
        else:
            print(' ', end='')
    print()

