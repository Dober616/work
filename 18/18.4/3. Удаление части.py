my_string = 'ПиТОн Это УдОБнО' # input('Введите строку: ')
lowers = [letter for letter in my_string if letter.islower()]
uppers = [letter for letter in my_string if letter.isupper()]
if lowers < uppers:
    print(my_string.lower())
else:
    print(my_string.upper())
