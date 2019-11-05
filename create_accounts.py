from com.abc.banking.account import Account
from com.abc.banking.minbalerror import MinBalNotMaintainedError
from traceback import print_exc

a = Account(acc_name='mehul chopra', acc_no=1234, acc_balance=10000)

try:
  ub = a.withdraw(500000)
except MinBalNotMaintainedError:
  # print traceback
  print_exc()
except ValueError:
  print_exc()
else:
  print(ub)


# avoid this
''' try:
  ub = a.withdraw(9500)
except Exception:
  # catch all exception block
  print_exc() '''