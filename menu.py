# every python file created is a module
# name -> menu

'''
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 1
Enter n: 8
0 1 1 2 3 5 8 13
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 2
Enter n : 6
0 2 4 6
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 3
Enter n : 10
Even
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 4
'''

# import the module
# import series

# directly import the functions from the module
from series import get_fibo_series as fibo, get_even_series


import math as m

while True:
  print('1. Fibo Series\n2. Even Series\n3. Even or Odd\n4. Exit')
  choice = int(input('Enter ur choice: '))

  if choice == 4:
    break # breaks out of the enclosing loop, forcibly

  n = int(input('Enter n: '))
  if choice == 1:
    # fibo series
    print(fibo(n))
    # pass # allows python to pass this as an empty block without raising a syntax error
  elif choice == 2:
    # even series
    print(get_even_series(n))
  else:
    # even or odd
    print(m.evenodd(n))