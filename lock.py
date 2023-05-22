import threading 
from socket import socket, AF_INET, SOCK_STREAM

class DistributedLock: 
<<<<<<< HEAD
  def __init__(self, hostname, port=1234):
=======
  def __init__(self, hostname, port):
>>>>>>> 1bb16283ffb992525535500ca3a0b39df6275f0b
    self._hostname = hostname
    self._port = port
    self._locked = False
    self._locked_by = None
<<<<<<< HEAD
    self._socket = None

  def acquire(self): 
    self._socket = socket(AF_INET, SOCK_STREAM)
    self._socket.connect((self._hostname, self._port))
    self._socket.send(b'acquire')
    response = self._socket.recv(1024).decode()

    if response == 'granted':
=======
    self._socket = socket(AF_INET, SOCK_STREAM)

  def acquire(self): 
    self._socket.connect((self._hostname, self._port))
    self._socket.send('acquire'.encode())
    response = self._socket.recv(1024).decode()

    if response == 'grated':
>>>>>>> 1bb16283ffb992525535500ca3a0b39df6275f0b
      self._locked = True
      self._locked_by = threading.current_thread().name

  def release(self):
    if self._locked:
<<<<<<< HEAD
      self._socket.send(b'release')
=======
      self._socket.send('release'.encode())
>>>>>>> 1bb16283ffb992525535500ca3a0b39df6275f0b
      self._socket.close()
      self._locked = False
      self._locked_by = None
  
  @property
  def locked(self):
    return self._locked
  
  @property
  def locked_by(self):
    return self._locked_by
    