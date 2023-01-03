import os

for element in os.listdir(os.path.abspath(os.path.join('..', '..', '..', 'dpo_python_basic'))):
    print(os.path.abspath(element))