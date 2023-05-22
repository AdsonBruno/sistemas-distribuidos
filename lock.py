import threading 
from socket import socket, AF_INET, SOCK_STREAM

class DistributedLock: 
  def __init__(self, hostname, port):
    self._hostname = hostname
    self._port = port
    self._locked = False
    self._locked_by = None
    self._socket = socket(AF_INET, SOCK_STREAM)

  def acquire(self): 
    self._socket.connect((self._hostname, self._port))
    self._socket.send('acquire'.encode())
    response = self._socket.recv(1024).decode()

    if response == 'grated':
      self._locked = True
      self._locked_by = threading.current_thread().name

  def release(self):
    if self._locked:
      self._socket.send('release'.encode())
      self._socket.close()
      self._locked = False
      self._locked_by = None
  
  @property
  def locked(self):
    return self._locked
  
  @property
  def locked_by(self):
    return self._locked_by
    