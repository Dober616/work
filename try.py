# my_dict = {1: 'f', 2: 's'}
#
# print(my_dict.get(3))

class MyDict:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_value(self, key):
        self.key = key
        result = self.dictionary.get(self.key)
        if result:
            return result
        return 0




my_dictionary = {1: 'a', 2: 'b'}

ttt = MyDict(my_dictionary)
print(ttt.get_value(3))
