# Developer X

# Square IS-A Shape
from .shape import Shape
class Square(Shape):
  def __init__(self, side):
    self.side = side

  # followed the protocol
  def area(self):
    return self.side ** 2

  def perimeter(self):
    return 4 * self.side