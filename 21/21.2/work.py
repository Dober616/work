def factorial(num):

    fact_n_minus_1 = factorial(num - 1)
    return num * fact_n_minus_1




num_fact = factorial(5)
print(num_fact)




# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой загловок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
