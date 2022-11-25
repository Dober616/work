
student = dict()
student_info = input('Введите данные о студенте через пробел: '
                'Фамилия, Имя, Город, Место учебы, Оценки: '
                )
student_string = student_info.split()
student['Фамилия'] = student_string[0]
student['Имя'] = student_string[1]
student['Город'] = student_string[2]
student['Место учебы'] = student_string[3]
student['Оценки'] = []
for marks in student_string[4:]:
    student['Оценки'].append(marks)



for data in student:
    print(data, '-', student[data])