def shift_symbols(word, shift):
    temp = word[len(word) - shift : len(word)] + word[0:len(word) - shift]
    return temp

text = 'vujgvmCfb tj ufscfu ouib z/vhm '
message = list(text.upper())
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message_numbers = [alfabet.index(letter) if letter in alfabet else letter for letter in message]
print(message_numbers)
print(shift_symbols(word, 3) for word in text)
new_message = [alfabet[(number + 25) % 26] if number in range(26) else number for number in message_numbers]
print(new_message)