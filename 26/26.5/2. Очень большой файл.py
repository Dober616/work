def numm_summ():
    with open('numbers.txt', 'r') as my_file:
        for line in my_file:
            numm = line.rstrip().split()
            for i in numm:
                clear_line = int(i)
                yield clear_line

for i in numm_summ():
    print(i, end=' ')





