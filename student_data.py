from com.abc.lib.student_ops import get_details, get_grade

name = input('Enter name: ')
roll = int(input('Enter roll: '))
gender = input('Enter gender: ')
marks = float(input('Enter marks: '))

# procedural style of calling functions
print(get_details(name=name, gender=gender, roll=roll, marks=marks))
print(get_grade(marks=marks))

