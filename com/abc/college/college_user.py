# CollegeUser -> object (single innheritance)
class CollegeUser(object): # every class in python implicitly inherits from the object class
  def __init__(self, name, gender, contact_nos):
    # self can be Student, Professor, any subclass of CollegeUser
    self.name = name
    self.gender = gender
    self.contact_nos = contact_nos

  def get_details(self):
    # self can be Student, Professoor, any subclass of CollegeUser
    part1 = 'Name : {0}\nGender: {1}\n'.format(self.name, self.gender)
    part2 = 'Contact Nos : '
    if self.contact_nos:
      part2 += '\n'.join(self.contact_nos)
    else:
      part2 += '\nNA'

    return part1 + part2

  # method overriding
  def __str__(self):
    return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)