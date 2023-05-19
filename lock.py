import threading

class Lock: 
  def __init__(self):
    self._lock = threading.Lock()
    self._locked = False
    self._locked_by = None
    self._request_queue = []

  def acquire(self): 
    self._lock.acquire()
    self._request_queue.append(threading.current_thread().name)
    while self._locked or self._request_queue[0] != threading.current_thread().name:
      self._lock.release()
      self._lock.acquire()
    
    self._locked = True
    self._locked_by = threading.current_thread().name
    self._lock.release()

  def release(self):
    self._lock.acquire()
    self._request_queue.pop(0)
    self._locked = False
    self._lock.release()

  def is_locked(self): 
    return self._locked

  def locked_by(self):
    return self._locked_by
    