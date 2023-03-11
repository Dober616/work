import re

text = 'AV - Analytics Vdhya AV'

result = re.match(r'AV', text)
print(f'Поиск в начале строки по шаблону: {result}')
print(result.group(0))
print(result.start())
print(result.end())
result = re.match(r'Analytics', text)
print(result)

print('=' * 40)
result = re.search(r'Analytics', text)
print(f'Поиск в строке по шаблону: {result}')
print(result.group(0))

print('=' * 40)

result = re.findall(r'AV', text)
print(f'Все совпадения по шаблону: {result}')

print('=' * 40)

text2 = 'AV is largest Analytics community of India. India!'

result = re.sub(r'India', 'the World', text2)
print(f'Замена всех найденных шаблонов: {result}')

print('=' * 40)

pattern = re.compile('AV')
result = pattern.findall(text)
print(result)
result2 = pattern.findall(text2)
print(result2)