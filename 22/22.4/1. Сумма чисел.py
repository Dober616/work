initial_file = open('numbers.txt', 'r')
result_list = [result.rstrip() for result in initial_file]
summ = 0
for result in result_list:
    summ += int(result)
print(summ)
final_file = open('results.txt', 'w')
final_file.write(str(summ))
initial_file.close()
final_file.close()