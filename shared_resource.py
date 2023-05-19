from lock import Lock

class SharedResource:
  def __init__(self):
    self._counter = 0
  
  def do_something(self):
    self._counter += 1
    print(f'Recurso compartilhado sendo utilizado. Contador: {self._counter}')
