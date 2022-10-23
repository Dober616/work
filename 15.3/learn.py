words = []
counts = [0, 0, 0]
for i in range(3):
    print('Введите ', i+1, 'слово: ', end='')
    word = input()
    words.append(word)
print(words)
text = input('Слово из текста: ')
while text != 'end':
    for index in range (3):
        if words[index] == text:
            counts [index] += 1
    text = input('Слово из текста: ')

print('Подсчет слов в тексте: ')
for t in range(3):
    print(words[t], ':\t', counts[t])