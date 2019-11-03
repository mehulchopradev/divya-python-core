# Developer Y

# Rectangle IS-A Shape
from .shape import Shape
class Rectangle:
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def area(self):
    return self.length * self.breadth

  def perimeter(self):
    return 2 * (self.length + self.breadth)