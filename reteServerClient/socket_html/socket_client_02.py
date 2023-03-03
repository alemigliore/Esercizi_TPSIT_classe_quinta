import socket
import sys
target_host = "info.cern.ch"
f = open("./fileHtml.txt", "w")

target_port = 80
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
client.send(request.encode())

response = client.recv(512)
while len(response) > 0:
    ind = 0
    string = response.decode()

    while string[ind] != '<':
        ind = ind + 1
        
    print(string[ind:])
    f.write(string[ind:])
    response = client.recv(512)

f.close()