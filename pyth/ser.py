import socket

host = 'localhost'
port = 500

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen(1)

c,addr= s.accept()

print("connection from :",str(addr))

c.send(b"hello client , how are u")
msg = "bye!"
c.send(msg.encode())

c.close()