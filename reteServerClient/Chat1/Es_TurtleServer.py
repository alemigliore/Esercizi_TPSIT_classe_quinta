from multiprocessing import connection
import socket
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5000))
s.listen()
print("In attesa di connessioni...")
connection, address = s.accept()

while True:
    data = s.recv(4096)
    stringa = data.decode()
    print(stringa)
    comando = stringa.split(",")
    if(comando[0] = "f"):
        t.forward(comando[1])
    
s.close()
