def abc():
  i = 3 # int object <- i (abc)

  # python a function can be defined inside another function
  def pqr(): # function object <- pqr (abc)
    print(i) # inner function can access enclosing function variables

  pqr()

abc()