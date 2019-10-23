n = int(input('Enter n: '))

# i = 0

# while loop
'''
while <<relational expression which yields python truthy/falsy>>:
  I1
  I2
  I3
'''
'''while i <= n:
  if not i % 2:
    print(i)
  i = i + 1'''

# for loop
'''
for v in <<sequence of elements>>:
  I1
  I2
  I3
'''
# Range 0 to n
# [0-n]
# n = 8 - [0, 1, 2, 3,,,,,8]

'''for v in range(0, n + 1):
  if not v % 2:
    print(v)'''
  
for v in range(0, n + 1, 2): # 3rd parameter - step size
  print(v)