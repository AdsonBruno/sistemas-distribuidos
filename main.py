from lock import Lock
import threading

def worker(lock):
  lock.acquire()
  locked_by = lock.locked_by()
  print('Bloqueio adquirido pela thread: ',  locked_by)
  lock.release()

def main():
  lock = Lock()

  thread = threading.Thread(target=worker, args=(lock,))
  thread.start()

  thread.join()
  
  lock.acquire()

  locked_by = lock.locked_by()
  print('Bloqueio adquirido pela thread: ',  locked_by)

  if lock.is_locked():
    print('Bloqueio adquirido')
  else: 
    print('Bloqueio não adquirido')
  
  lock.release()

if __name__ == '__main__':
  main()
      