# user defined exception class

class MinBalNotMaintainedError(Exception):
  def __init__(self, message):
    super().__init__(message)