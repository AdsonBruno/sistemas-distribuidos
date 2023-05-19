from lock import Lock

class SharedResource:
  def __init__(self, lock):
    self._counter = 0
    self._lock = lock
  
  def do_something(self):
    with self._lock:
      self._counter += 1
      print(f'Recurso "compartilhado sendo utilizado. Contador: {self._counter}')
