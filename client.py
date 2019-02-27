import socket

s = socket.socket()
s.connect( ('localhost', 1234) )

msj = "hola desde el cliente .."
s.send(msj.encode())

response = s.recv(1024).decode()

print (response)
s.close()