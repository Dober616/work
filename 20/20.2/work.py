def add_numm(seq, number):
    seq = list(seq)
    for i in range(len(seq)):
        seq[i] += number
    return seq

origin_tupple = (1, 3, 4, 6, 7)
changed_list = add_numm(origin_tupple, 2)

print(origin_tupple)
print(changed_list)