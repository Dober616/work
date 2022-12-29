import os

for element in os.listdir(os.path.join('..', '..', '..', 'work')):
    print(os.path.join(os.path.abspath('..'), element))
    