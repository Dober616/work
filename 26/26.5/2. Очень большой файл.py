

def numbers(text):
    return [int(number) for number in text.rstrip().split()]

def file_reader():

    with open('numbers.txt', 'r') as file:
        sum = 0
        for line in file:
            sum += int(line)
            yield sum

for i in file_reader():
    print(i)