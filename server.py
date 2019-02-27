import socket

s = socket.socket()
s.bind( ('localhost', 1234) )
s.listen(5)
print ("servidor socket ejecutandose en puerto 1234 ..")

while True:
    conn, addr = s.accept()
    print ("Nueva conexion establecida ..")
    print (addr)

    request = conn.recv(1024).decode()
    print (request)

    msj = "saludo desde servidor .."
    conn.send(msj.encode())
    conn.close()

