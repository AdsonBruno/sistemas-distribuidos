import threading

class Lock: 
  def __init__(self):
    self._lock = threading.Lock()
    self._locked = False
    self._locked_by = None

  def acquire(self): 
    self._lock.acquire()
    while self._locked:
      self._lock.release()
      self._lock.acquire()
    
    self._locked = True
    self._locked_by = threading.current_thread().name

  def release(self):
    self._locked = False
    self._lock.release()

  def is_locked(self): 
    return self._locked

  def locked_by(self):
    return self._locked_by
    