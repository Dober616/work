main = [1,0,1,1,1,1,0,1,0,1,1,1,0,1]
first_company = [0,0,0]
second_company = [1,0,0,1,1]
third_company = [1,1,1,0,1]
bed_tasks = 0
main.extend(first_company)
main.extend(second_company)
main.extend(third_company)
print(main)
for task in main:
    if task == 0:
        bed_tasks += 1

print('Невыполненных задач: ', bed_tasks)

