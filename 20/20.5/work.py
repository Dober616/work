phone_book = {
    ('Ivan', 'Ivanov'): 89123456,
    ('Ivan', 'Petrov'): 89456789,
    ('Petr', 'Ivanov'): 89234567,
    ('Egor', 'Egorov'): 89345678
}

phone_book[('Eger', 'Egorov')] = 89765432

print(phone_book)
for men in phone_book:
    if 'Ivanov' in men:
        print(men)
