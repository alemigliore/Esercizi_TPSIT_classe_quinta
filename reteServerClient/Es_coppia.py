import socket
#                         IPv4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
stringa = str(input("ale:"))
#encode trasforma la stringa in binerio
s.sendto(stringa.encode(),("192.168.0.126", 5000))

#recvform ritorna sia i dati che l'indirizzo del client
s.bind(("192.168.0.122", 5000))
while True:
    dati, ind_client = s.recvfrom(4096) #4096 è la dimensione in byte del buffer di ricezione
    if(dati.decode() == "exit"):
        exit()
    print(f"Elia: {dati.decode()}")