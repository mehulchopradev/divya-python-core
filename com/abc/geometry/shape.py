# Abstract classes and Abstract methods
# in order for the sub classes to compulsorily follow the protocol
# 1. Mark ur class as abstract
# 2. Mark the protocol methods as abstract too

# In python, an object cannot be created of an abstract class with absract methods

from abc import ABC, abstractmethod

class Shape(ABC):

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass