import threading

class Lock: 
  def __init__(self):
    self._lock = threading.Lock()
    self._locked = False

  def is_locked(self): 
    return self._locked

    