# for every class in python (user defined / built in), an object is created in the memory during program load
'''
class objects
str -> object
int -> object
Student -> object - class object attributes
'''

class Student:

  count = 0 # class attribute
  # access class attribute using the class name
  # Student.count

  def __init__(self, name, gender, roll, marks):
    # create attributes in the self objects
    # constructor

    # object attributes
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    Student.count += 1

  def get_details(self):
    # self - address of the current Student object for which get_details was called
    return 'Name: ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + str(self.roll) \
    + '\nMarks: ' + str(self.marks)

  def get_grade(self):
    # s1, s2, s3, ... Student object
    marks = self.marks
    if marks > 100 or marks < 0:
      grade = 'I'
    elif marks >= 70:
      grade = 'A'
    elif marks >= 60:
      grade = 'B'
    elif marks >= 40:
      grade = 'C'
    else:
      grade = 'F'
    
    return grade