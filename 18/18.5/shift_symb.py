def shift_symbols():
    temp = my_word[shift:len(my_word)] + my_word[0:shift]
    return temp

my_words_list = []
my_word = 'uibo'
for shift in range(len(my_word)):
    my_words_list.append(shift_symbols())

print(my_words_list)
