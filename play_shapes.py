# Manager

from com.abc.geometry.square import Square
from com.abc.geometry.shape import Shape
from com.abc.geometry.rectangle import Rectangle
from com.xyz.geometry.shape_stats import ShapeStats

s = Square(side=5)
r = Rectangle(length=5, breadth=3)

''' print(s.area())
print(s.perimeter()) '''

if isinstance(s, Shape): # whether s (square) inherits from Shape or no
  ShapeStats.print_stats(s)

if isinstance(r, Shape):
  ShapeStats.print_stats(r)