# def histogram(string):
#     sym_dict = dict()
#     for sym in string:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1
#     return sym_dict
#
#
# text = input('Введите текст: ').lower()
# hist = histogram(text)
# for i in sorted(hist.keys()):
#     print(i, '-', hist[i])
#
# print('Максимальная частота: ', max(hist.values()))

# old_sim = {'Кирилл':89097969666,
#            'Егор':89114505878,
#            'Катя':89097771999
# }
# new_sim = {'Батя':89114665591,
#            'Бабушка':89114747474,
#            'Аня':89216778396
# }
#
# old_sim.update(new_sim)
#
# old_sim['Максим'] = old_sim.pop('Егор')
# for i in sorted(old_sim.keys()):
#     print(i, '\t:', old_sim[i])
#
# print(old_sim.get('Степан'))
