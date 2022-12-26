import os

for element in os.listdir('..'):
    print(os.path.join(os.path.abspath('..'), element))
    