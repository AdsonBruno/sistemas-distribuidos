import threading

class Lock: 
  def __init__(self):
    self._lock = threading.Lock()
    self._locked = False

  def acquire(self): 
    self._lock.acquire()
    while self._locked:
      self._lock.release()
      self._lock.acquire()
    self._locked = True
    self._lock.release()


  def is_locked(self): 
    return self._locked

    