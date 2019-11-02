pointers = [10, 10, 4, 5, 3, 1, 8, 9, 10]

# get a new list of only the odd pointers from pointers list (filtering)
# functional programming

# filtering criteria function (lower order function)
'''def odd(ele):
  return ele % 2

# higher order function
odds = list(filter(odd, pointers))
print(odds) '''

odds = list(filter(lambda ele: ele % 2, pointers))
print(odds)

# internal
''' def filter(func, elements):
  result = []
  for element in elements:
    if func(element):
      result.append(element)
  return result '''

# get a new list of even elements greater than 5 from pointers list (filtering)

# criteria (lower order function)
''' def even_greater_than_5(ele):
  return not ele % 2 and ele > 5

evens = list(filter(even_greater_than_5, pointers))
print(evens) '''

evens = list(filter(lambda ele: not ele % 2 and ele > 5, pointers))
print(evens)


# get a new list of squares of elements from pointers list (mapping)
# lower order function (mapping)

''' def squares(ele):
  return ele ** 2
sq = list(map(squares, pointers))
print(sq) '''

sq = list(map(lambda ele: ele ** 2, pointers))
print(sq)

# Internally
''' def map(func, elements):
  result = []
  for element in elements:
    result.append(func(element))
  
  return result '''

# get a new list of deducted by 1 pointer from pointers list (mapping)
# lower order function

''' def deduct_by_one(ele):
  return ele - 1
deducted_marks = list(map(deduct_by_one, pointers))
print(deducted_marks)'''

deducted_marks = list(map(lambda ele: ele - 1, pointers))
print(deducted_marks)

# Pre requisite : Lower order function must have only one expression which is returns
# Lambda functions (annonymous functions)