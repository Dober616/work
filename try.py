def shift_symbols(my_word, shift):
    temp = my_word[shift:len(my_word)] + my_word[0:shift]
    return temp
def caesar(letter_shift, my_word):
    encrypted_word = (alfabet[alfabet.index(letter) + 25) % len(alfabet) + letter_shift]
                         if letter in alfabet else letter for letter in my_word]
    return encrypted_word

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = 'fTjnqm tj scfuuf ibou fy/dpnqm'
message = list(text.upper())
