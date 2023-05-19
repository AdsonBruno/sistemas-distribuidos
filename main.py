from lock import Lock
from shared_resource import SharedResource
import threading

def worker(lock, resource):
  lock.acquire()
  locked_by = lock.locked_by()
  print(f'Bloqueio adquirido pela thread: {locked_by}')
  resource.do_something()
  lock.release()

def main():
  lock = Lock()
  resource = SharedResource(lock)

  thread = threading.Thread(target=worker, args=(lock, resource))

  thread.start()
  thread.join()

  lock.acquire()

  locked_by = lock.locked_by()
  print(f'Bloqueio adquirido pela thread: {locked_by}')

  if lock.is_locked():
    print('Bloqueio adquirido')
  else: 
    print('Bloqueio não adquirido')
  
  lock.release()

if __name__ == '__main__':
  main()
      