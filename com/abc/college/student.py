# Student IS-A CollegeUser
# subclass IS-A superclasss
# child class IS-A parentclass

# Inheritance
from .college_user import CollegeUser

class Student(CollegeUser):
  def __init__(self, name, gender, roll, marks, contact_nos=None):
    super().__init__(name, gender, contact_nos)
    # Internally
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.roll = roll
    self.marks = marks