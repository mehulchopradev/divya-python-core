from com.abc.college.student import Student
print(Student.count)
s1 = Student('mehul', 'm', 10, 45) # 4003 -> Student
# Internally
# 1. 4003 -> Student object
# 2. Student.__init__(4003 'mehul', 'm', 10, 45)

# create attributes in an object
'''s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 45'''


s2 = Student('divya', 'f', 12, 94) # 4001 -> Student
# Internally
# 1. 4001 -> Student object
# 2. Student.__init__(4001)

'''s2.name = 'divya'
s2.gender = 'f'
s2.roll = 12
s2.marks = 94'''

print(Student.count)

s3 = Student('jane', 'f', 5, 68) # 4004 -> Student
'''s3.student_name = 'jane'
s3.gen = 'f'
s3.r = 5
s3.marks = 68'''
s3.ac = 'xyz' # specific object along with the compulsory set of attributes can have its own attributes also

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

print(s1.get_grade())
# Internally
# Student.get_grade(s1)

print(s2.get_grade())
# Internally
# Student.get_grade(s2)

print(s3.get_details())
# Student.get_details(s3)

print(Student.count)