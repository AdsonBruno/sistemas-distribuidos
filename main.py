from lock import DistributedLock
from shared_resource import SharedResource
import threading

def worker(lock, resource):
  with lock:
    locked_by = lock.locked_by()
    print(f'Bloqueio adquirido pela thread: {locked_by}')
    resource.do_something()
    resource.release()

def main():
  hostname = 'localhost'
  port = 5000

  lock = DistributedLock(hostname, port)
  resource = SharedResource()

  thread = threading.Thread(target=worker, args=(lock, resource))

  thread.start()
  thread.join()


  locked_by = lock.locked_by()
  print(f'Bloqueio adquirido pela thread: {locked_by}')

  if lock.locked:
    print('Bloqueio adquirido')
  else: 
    print('Bloqueio não adquirido')
  
  lock.release()

  if lock.locked:
    print('Recurso ainda está bloqueado')
  else:
    print('Recurso está liberado')

if __name__ == '__main__':
  main()
      