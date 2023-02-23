for raw in range(1, 10):
    for col in range(1, 10):
        if col % 3 == 0:
            print(col, end=' ')
        else:
            print(raw, end=' ')
    print()
