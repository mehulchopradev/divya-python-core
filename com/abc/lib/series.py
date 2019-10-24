# name -> com.abc.lib.series
def get_fibo_series(n):
  # '0 1 1 2 3 5 8 13'
  result = ''
  a, b = 0, 1
  result = result + str(a) + '\t' + str(b) + '\t'

  for v in range(3, n + 1):
    c = a + b
    result = result + str(c) + '\t'
    a, b = b, c

  return result


def get_even_series(n):
  # '0 2 4 6 8 10'
  result = ''
  for v in range(0, n + 1, 2):
    result = result + str(v) + '\t'
  
  return result