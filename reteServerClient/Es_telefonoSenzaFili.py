import socket
#                         IPv4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("192.168.0.122", 5000))
while True:
    dati, ind_client = s.recvfrom(4096) #4096 è la dimensione in byte del buffer di ricezione
    print(f"{dati.decode()} ricevuti da {ind_client}")
    stringa = dati
    s.sendto(stringa,("192.168.0.131", 5000))
        