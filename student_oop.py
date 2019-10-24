from com.abc.college.student import Student

s1 = Student() # 4003 -> Student
# create attributes in an object
s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90



s2 = Student() # 4001 -> Student
s2.name = 'divya'
s2.gender = 'f'
s2.roll = 12
s2.marks = 94

name = 'mehul chopra' # 5004 -> str
age = 32 # 6003 -> int

# access the attriutes from an object
'''print(s1.name)
print(s1.gender)

print(s2.name)
print(s2.gender)'''


print(s1.get_details())
# Internally
# Student.get_details(s1)

print(s2.get_details())
# Internally
# Student.get_details(s2)