from com.abc.college.student import Student
from com.abc.college.professor import Professor

s = Student('mehul', 'm', 10, 90)
p = Professor('jane', 'f', ['Physics'], ['987867868', '878798979'])
i = 10

print(i)
# Innternally
# print(i.__str__())
# print(int.__str__(i))

print(s)
# Internally
# print(s.__str__())
# print(Student.__str__(s))

print(p)

''' print(s.name)
print(s.gender)
print(s.roll)

print(p.name)
print(p.gender)
print(p.subjects) '''

print(s.get_details())
# Student.get_details(s)

print(p.get_details())
# Professor.get_details(p)