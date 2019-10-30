pointers = [4, 5, 5, 10, 2, 3, 2, 1, 6, 7]

# get a new list of even elements from the pointers list (filtering)
'''evens = []
for pointer in pointers:
  if not pointer % 2:
    evens.append(pointer)'''

# for comprehensions syntax
evens = [pointer for pointer in pointers if not pointer % 2]
print(evens)

# get a new list of odd elements greater than 3 from pointers list (filtering)
odds = [pointer for pointer in pointers if pointer % 2 and pointer > 3]
print(odds)

# get a new list of squares of elements from the pointers list (mapping)
squares = [pointer ** 2 for pointer in pointers]
print(squares)

# get a new list of cubes of even pointers greater than 5 from the pointers list (filtering + mapping)
cubes = [pointer ** 3 for pointer in pointers if not pointer % 2 and pointer > 5]
print(cubes)