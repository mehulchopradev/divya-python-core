n = int(input('Enter n: '))

# n = 8
'''
0 a
1 b a
1 c b a
2   c b
3     c
5
8
13
'''

a, b = 0, 1
print(a)
print(b)

# [3-9] : [3,4,5,6,7,8]
for v in range(3, n + 1):
  c = a + b
  print(c)
  a, b = b, c