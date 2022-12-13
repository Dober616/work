def add_num(seq, number):
    seq = list(seq)
    for i_num in range(len(seq)):
        seq[i_num] += number
    return seq


origin_tupple = (3, 1, 4, 1, 5)
changed_list = add_num(origin_tupple, 5)
add_num(changed_list, 5)
print(origin_tupple)
print(changed_list)
