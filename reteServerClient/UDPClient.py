import socket
#                         IPv4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    #encode trasforma la stringa in binerio
    stringa = input("inserisci una stringa: ")
    s.sendto(stringa.encode(),("192.168.0.136", 5000))