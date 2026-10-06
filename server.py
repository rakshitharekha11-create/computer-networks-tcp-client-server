import socket
from datetime import datetime
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),6060))
s.listen(5)

while True:
  clientSocket, address=s.accept()
  start_time=datetime.now()
  print(f"connection established from {address}")
  print(f"connection time:{start_time}")
  clientSocket.send(bytes("Welcome to the server!!!","utf-8"))
  clientSocket.recv(1024)
  
  end_time=datetime.now()
  duration=end_time-start_time
  print(f"connection duration:{duration.total_seconds():.2f}seconds")
  clientSocket.close()