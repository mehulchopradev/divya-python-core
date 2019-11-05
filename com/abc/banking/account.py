from .minbalerror import MinBalNotMaintainedError

class Account:
  minbalance = 1000

  def __init__(self, acc_name, acc_no, acc_balance):
    self.acc_name = acc_name
    self.acc_no = acc_no
    self.acc_balance = acc_balance

  def withdraw(self, amt):
    print('Transaction starts')

    '''
    try - except
    try - except - else
    try - except - finally
    try - except - else - finally
    try - finally
    '''

    try:
      if amt <= 0:
        raise ValueError('Amt to withdraw must be greater than 0')
      if self.acc_balance - amt < Account.minbalance:
        # raise an error to the caller of the withdraw method
        raise MinBalNotMaintainedError('Acc balance going below {0}'.format(Account.minbalance))

      self.acc_balance -= amt
      return self.acc_balance
    finally:
      # will execute irrespective of whether an error occured in the corresponding try or did not
      # even before the return statement it will execute

      # code usually will be the one that releases resources that were occupied previously
      # closing connection to server, closing connection to file system
      print('Transaction ends')