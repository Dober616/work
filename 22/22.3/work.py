
speakers_file = open('speakers.txt', 'r')
# data = speakers_file.read()
# print(data)
for line in speakers_file:
    print(line, end='')
speakers_file.close()
