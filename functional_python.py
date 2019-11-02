def abc(): # function object <- abc (module)
  i = 3 # int object <- i (abc)
  j = 4 # int object <- j (abc)
  k = 6

  # python a function can be defined inside another function
  def pqr(): # function object <- pqr (abc)
    print(i) # inner function can access enclosing function variables
    j = 5 # int object <- j (pqr)
    print(j) # 5

    # k = k + 7 # will not work
    # print(k)

  pqr()
  print(j) # 4

abc()

def mno(): # function object <- mno (module)
  i = 10 # int object <- i (abc)

  def pqr(n): # function object <- pqr (mno)
    return i + n

  # in python a function can return another function
  return pqr

m = mno()
# function object <- m (module)
print(m(5)) # <- pqr(5)

def xyz(f): # function object <- xyz (module)
  i = 10
  j = f(i) # f(i) <- abcc(i)
  return j + 5

def abcc(e): # function object <- abcc (module)
  return e + 10

print(xyz(abcc)) # in python a function can be passed as an argument to another function
# callback functions