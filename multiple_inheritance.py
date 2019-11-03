# Vendor x
class A:
  def fun(self):
    print('fun of A')

# Vendor y
class B:
  def show(self):
    print('show of B')

  def fun(self):
    print('fun of B')


# company abc

# one subclass having more than 1 super class
class C(A, B): # MRO (Method Resolution order)
  pass

c = C()
c.show()
c.fun()
