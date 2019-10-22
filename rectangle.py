def area_rectangle(length, breadth):
  a = length * breadth
  return a

def perimeter_rectangle(length, breadth):
  p = 2 * (length + breadth)
  return p

l = float(input('Enter length: ')) # int(), bool(), str()
b = float(input('Enter breadth: '))

a = area_rectangle(length=l, breadth=b)
p = perimeter_rectangle(length=l, breadth=b)

# built in functions (BIF's)
print(a)
print(p)