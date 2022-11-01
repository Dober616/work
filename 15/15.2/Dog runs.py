def score_table(n):
	table = []
	for _ in range(n):
		dog_score = int(input('Введите очки собаки: '))
		table.append(dog_score)
	return table
def max_index():
	max = final_table[0]
	hight_index = 0
	for index, i in enumerate(final_table):
		if max > i:
			max = i
			hight_index = index
	return hight_index
def min_index():
	min = final_table[0]
	low_index = 0
	for index, y in enumerate(final_table):
		if min < y:
			min = y
			low_index = index
	return index

n = int(input('Введите количество собак: '))
final_table = score_table(n)
print()
print('Начальная таблица', final_table)
print()
print('Максимальное количество очков: ', max_index())
print('Минимальное количество очков: ', min_index())

final_table[min_index()], final_table[max_index()] = final_table[max_index()], final_table[min_index()]
print(final_table)
