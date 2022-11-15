# def word_count(temp_word):
#     count = 0
#     for text_part in my_text.split():
#         if temp_word == text_part:
#             count += 1
#     return count
# words_list = input('Введите слово {word} через пробел: ').split()
#
# my_text = 'каждый охотник желает знать где сидит каждый охотник'
# for i in range(len(words_list)):
#     # words_count = ['-'.join([word for word in words_list], word_count(words_list[i]))]
#     print(words_list[i], word_count(words_list[i]))
#
# print(words_list)
text = 'каждый охотник желает знать где желает охотник'
words_list = [input('Введите слово: ') for _ in range(3)]
word_count = [text.count(word) for word in words_list]
print(word_count)