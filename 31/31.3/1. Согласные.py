import re

text = 'Even if they djinns, I will get djinns that can outdjinn them'
result = re.findall(r'\b[aeiouAEIOU]\w+', text)
print(result)
result = re.findall(r'\b[^aeiouAEIOU]\w+', text)
print(result)