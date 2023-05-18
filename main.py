from lock import Lock

def main():
  lock = Lock()

  lock.acquire()

  if lock.is_locked():
    print('Bloqueio adquirido')
  else: 
    print('Bloqueio não adquirido')
  
  lock.release()

if __name__ == '__main__':
  main()
      