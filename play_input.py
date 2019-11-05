print('Program starts')

n = input('Enter n : ')

# Exception handling
try:
  ii = int(n)
except ValueError:
  print('Please enter integer value')
else:
  # will execute when there is no exception raised in the corresponding try block
  print('Odd') if ii % 2 else print('Even')

print('Program ends')