import socket
#                         IPv4              UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#legare il socket ad un IP ed ad una porta con il metodo BIND
#IP (stringa) e PORTA (numero) vanno inseriti in una tupla

s.bind(("0.0.0.0", 5000)) #SOLO SUI SERVER / 0.0.0.0 per prendere automaticamente l' ip del pc server

#recvform ritorna sia i dati che l'indirizzo del client
while True:
    dati, ind_client = s.recvfrom(4096) #4096 è la dimensione in byte del buffer di ricezione
    if(dati.decode() == "exit"):
        exit()
    print(f"{dati.decode()} ricevuti da {ind_client}")