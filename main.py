from lock import Lock

def main():
  lock = Lock()

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
      