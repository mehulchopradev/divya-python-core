# accept variable number of arguments (0 to n)
def myadd(*args):
  # print(args) # args -> tuple object
  sum = 0
  for arg in args:
    sum += arg
  return sum


# positional arguments packing
print(myadd()) # 0
print(myadd(5)) # 5
print(myadd(4, 5, 1)) # 10
print(myadd(5, 6, 3, 4, 6, 7, 8))

def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = (5, 2.3) # could be even a list

print(perimeter(stats[0], stats[-1]))

# the elements in the data structure were in the same order as the positional arguments needed by the function
print(perimeter(*stats)) # positional arguments unpacking

def area(**rect_stats):
  # print(rect_stats) # rect_stats -> dict
  return rect_stats['length'] * rect_stats['breadth']

# print(area(5.1, 5.0))

# keyword arguments packing
print(area(length=5.1, breadth=5.0))
# print(area(len=9, bre=5)) # this is not going to work

stats_map = {'breadth': 4, 'length': 6}

print(perimeter(stats_map['length'], stats_map['breadth']))

# key names of the items in the dict match with the parameter names in the function
print(perimeter(**stats_map))