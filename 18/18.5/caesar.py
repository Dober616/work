def shift_symbols():
    temp = word[shift:len(word)] + word[0:shift]
    return temp

def caesar():
    encrypted_message = [alfabet[alfabet.index(letter) - len(alfabet) + 51]
                         if letter in alfabet else letter for letter in my_word]
    return encrypted_message


word = 'vujgvmCfb tj ufscfu ouib z/vhm '
alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
my_words_list = []
for shift in range(len(word)):
    my_words_list.append(shift_symbols())
count = 0
for my_word in my_words_list:
    print(count)
    print(my_word, '===================', ''.join(caesar()))
    count += 1




