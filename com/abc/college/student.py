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

  def __init__(self, name, gender, roll, marks, contact_nos=None):
    # None means no address. Variable exists but does not store any address
    # create attributes in the self objects
    # constructor

    # object attributes
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks
    self.contact_nos = contact_nos

    Student.count += 1

  def get_details(self):
    # self - address of the current Student object for which get_details was called
    part1 = 'Name: ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + str(self.roll) \
    + '\nMarks: ' + str(self.marks) + '\n'

    part2 = 'Contact Nos :\n'
    if self.contact_nos:
      # get into the if, when contact_nos list has atleast 1 element
      for contact_no in self.contact_nos:
        part2 += contact_no + '\n'
    else:
      # contact_nos is None
      # contact_nos is []
      part2 += 'NA'
    
    return part1 + part2

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

  def get_name_roll(self):
    return (self.name, self.roll) # tuple object