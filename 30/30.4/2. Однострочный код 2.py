my_string = 'qWe456trY'
print(list(filter(lambda x: not (x.isupper() or x.isdigit()), my_string)))