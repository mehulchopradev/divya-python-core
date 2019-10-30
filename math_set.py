m1 = [1, 3, 5, 10]
m2 = [3, 6, 5, 4]

# common set of pointers
commons = []
for a in m1:
  if a in m2:
    commons.append(a)

print(commons)