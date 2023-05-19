import threading

class Lock: 
  def __init__(self):
    self._lock = threading.Lock()
    self._locked = False
    self._locked_by = None
    self._request_queue = []

  def acquire(self): 
    thread = threading.current_thread().name
    self._lock.acquire()

    self._request_queue.append(thread)
    while self._locked and self._locked_by != thread:
      if thread not in self._request_queue:
        self._request_queue.append(thread)
      self._lock.release()
      self._lock.acquire()
    
    self._locked = True
    self._locked_by = thread
    
    if thread in self._request_queue:
      self._request_queue.remove(thread)
    
    self._lock.release()

  def release(self):
    self._lock.acquire()
    self._locked = False

    if self._request_queue:
      next_thread = self._request_queue[0]
      self._locked = True
      self._locked_by = next_thread
      self._request_queue.remove(next_thread)

    self._lock.release()

  def is_locked(self): 
    return self._locked

  def locked_by(self):
    return self._locked_by
  
  def __enter__(self):
      self.acquire()

  def __exit__(self, exc_type, exc_value, traceback):
      self.release()

  