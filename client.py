import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),6060))
message=s.recv(2048)
print(f"Message received:{message.decode()}")
time.sleep(2)
s.send(bytes("Connection Completed","utf-8"))
s.close()