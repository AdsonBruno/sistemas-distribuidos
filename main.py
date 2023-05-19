from lock import Lock
from shared_resource import SharedResource
import threading

def worker(lock, resource):
  with lock:
    locked_by = lock.locked_by()
    print(f'Bloqueio adquirido pela thread: {locked_by}')
    resource.do_something()

def main():
  lock = Lock()
  resource = SharedResource()

  thread = threading.Thread(target=worker, args=(lock, resource))

  thread.start()
  thread.join()


  locked_by = lock.locked_by()
  print(f'Bloqueio adquirido pela thread: {locked_by}')

  if lock.is_locked():
    print('Bloqueio adquirido')
  else: 
    print('Bloqueio não adquirido')
  
  lock.release()

  if lock.is_locked():
    print('Recurso ainda está bloqueado')
  else:
    print('Recurso está liberado')

if __name__ == '__main__':
  main()
      