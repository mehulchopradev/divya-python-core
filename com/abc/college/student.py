# Student IS-A CollegeUser
# subclass IS-A superclasss
# child class IS-A parentclass

# Inheritance
from .college_user import CollegeUser
# Student -> CollegeUser -> object (multilevel inheritance)
class Student(CollegeUser):
  def __init__(self, name, gender, roll, marks, contact_nos=None):
    super().__init__(name, gender, contact_nos)
    # Internally
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.roll = roll
    self.marks = marks

  # method overriding
  # the signature of the overriden methood and inherited method must be the same
  def get_details(self):
    part1 = super().get_details()
    # Internally
    # part1 = CollegeUser.get_details(self)

    part2 = '\nRoll : {0}'.format(self.roll)

    return part1 + part2