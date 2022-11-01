def punctuation(message):
    message_count = 0
    for symbol in message:
        if symbol == '!' or symbol == '?':
            message_count += 1
    return message_count
first_message = input('Введите первое сообщение: ')
second_message = input('Введите второе сообщение: ')
first_message_count = punctuation(first_message)
second_message_count = punctuation(second_message)
if first_message_count > second_message_count:
    print('Третье сообщение: ', first_message, second_message)
elif first_message_count > second_message_count:
    print('Третье сообщение: ', second_message, first_message)
else:
    print('Ой!!!')


