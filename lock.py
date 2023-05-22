import threading 
from socket import socket, AF_INET, SOCK_STREAM

class DistributedLock: 
  def __init__(self, hostname, port=1234):
    self._hostname = hostname
    self._port = port
    self._locked = False
    self._locked_by = None
    self._socket = None

  def acquire(self): 
    self._socket = socket(AF_INET, SOCK_STREAM)
    self._socket.connect((self._hostname, self._port))
    self._socket.send(b'acquire')
    response = self._socket.recv(1024).decode()

    if response == 'granted':
      self._locked = True
      self._locked_by = threading.current_thread().name

  def release(self):
    if self._locked:
      self._socket.send(b'release')
      self._socket.close()
      self._locked = False
      self._locked_by = None
  
  @property
  def locked(self):
    return self._locked
  
  @property
  def locked_by(self):
    return self._locked_by
    