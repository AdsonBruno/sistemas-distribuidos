from lock import DistributedLock
from threading import Condition

class SharedResource:
  def __init__(self):
    self._counter = 0
    self._lock = DistributedLock('localhost', 5000)
    self._lock.acquire()

  def do_something(self):
    with self._lock:
      self._counter += 1
      # while self._counter > 0:
      #   self._condition.wait()
      # self._counter += 1
      print(f'Recurso "compartilhado sendo utilizado. Contador: {self._counter}')

  def release(self): 
    with self._lock:
      self._counter -= 1
      if self._counter == 0:
        self._lock.release()