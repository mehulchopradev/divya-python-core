from com.abc.college.student import Student

'''slist = [
  Student('mehul', 'm', 10, 90),
  Student('divya', 'f', 5, 92),
  Student('jane', 'f', 23, 90)
]

roll = int(input('Enter roll to search: '))

# in python a for loop/while loop can have an else block
for student in slist:
  if student.roll == roll:
    print(student.get_details())
    break
else:
  # executes when the corresponding for block has been completely exhausted
  # executes when there is no break statement executed in the corresponding for block
  print('Not found') '''

smap = {
  10: Student('mehul', 'm', 10, 90),
  5: Student('divya', 'f', 5, 92),
  23: Student('jane', 'f', 23, 90)
}

roll = int(input('Enter roll to search: '))

if roll in smap:
  student = smap[roll]
  print(student.get_details())
else:
  print('Not found')