def symb_count():
    for i in text.lower():
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1
    return text_dict

text = input('Введите текст: ')
text_dict = dict()
count = symb_count()
for i in sorted(count.keys()):
    print(i, ':', count[i])
print('Максимальное значение: ', max(count.values()))