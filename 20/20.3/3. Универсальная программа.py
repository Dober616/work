def crypto(text):
    res = []
    if isinstance(text, dict):
        text = text.items()
    for index, value in enumerate(text):
        if index % 2 == 0:
            res.append(value)
    return res


my_string = input('Введите строку: ')
print(crypto(my_string))
