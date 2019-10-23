n = int(input('Enter n: '))

# if - else
'''
if <<relational expression which yields a python truthy/falsy value>>:
      I1
  I2
else:
  I1
  I2
  I3
'''

'''if n % 2:
  print('It is odd')
else:
  print('It is even')'''

# if comprehensions
# 2 branches and both branches must have only single instruction to execute
print('Odd') if n % 2 else print('Even')