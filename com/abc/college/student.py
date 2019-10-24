class Student:

  def get_details(self):
    # self - address of the current Student object for which get_details was called
    return 'Name: ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + str(self.roll) \
    + '\nMarks: ' + str(self.marks)