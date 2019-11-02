# Professor IS-A CollegeUser

from .college_user import CollegeUser

class Professor(CollegeUser):
  def __init__(self, name, gender, subjects, contact_nos=None):
    super().__init__(name, gender, contact_nos)
    # Internally
    # CollegeUser.__init__(name, gender, contact_nos)
    self.subjects = subjects