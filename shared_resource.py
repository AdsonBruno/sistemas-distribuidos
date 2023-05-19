from lock import Lock
from threading import Condition

class SharedResource:
  def __init__(self):
    self._counter = 0
    self._lock = Lock()
    self._condition = Condition(self._lock)
  
  def do_something(self):
    with self._lock:
      while self._counter > 0:
        self._condition.wait()
      self._counter += 1
      print(f'Recurso "compartilhado sendo utilizado. Contador: {self._counter}')

  def release(self): 
    with self._lock:
      self._counter -= 1
      if self._counter == 0:
        self._condition.notify