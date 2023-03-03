#lettura database
import sqlite3
import socket
from threading import Thread
def caricaDati():
    connectionDB = sqlite3.connect('file.db')
    cursor = connectionDB.cursor()
    res = cursor.execute('SELECT * FROM files')
    files = res.fetchall()
    print(files)
    res = cursor.execute('SELECT * FROM frammenti')
    return files

#inizializzazione socket TCP con thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listaThread = []

s.bind(("127.0.0.1", 8000))
s.listen()

while True:
    connection, address = s.accept()
    print(f"Connesso con {address}")
    client = Client(connection)
    client.start()
    listaThread.append(client)

    for thread in listaThread:
        if not thread.running:
            thread.join()
            listaThread.remove(thread)

#classe thread
class Client(Thread):
    def __init__(self, connection):
        Thread.__init__(self)
        self.running = True
        self.connection = connection

        #self.files, self.frammenti = caricaDati()

    def run(self):
        while self.running:
            # codOperazione,nomeFile(,id_frammento)
            msgR = self.connection.recv(4096)
            msgR = msgR.decode()
            msgR = msgR.split(',')
            '''if int(msgR[0]) == 1:
                if isPresente(self.files, msgR[1]):
                    self.connection.sendall("Il file è presente".encode())
                else:
                    self.connection.sendall("Il file non è presente".encode())
            elif int(msgR[0]) == 2:
                numero = numeroFrammenti(self.files, msgR[1])
                self.connection.sendall(
                    ("numero frammenti: "+str(numero)).encode())
            elif int(msgR[0]) == 3:
                host = ipHost(msgR[1], msgR[2])
                self.connection.sendall(
                    ("host contentente il frammento: "+str(host)).encode())
            elif int(msgR[0]) == 4:
                stringa = allIpHosts(msgR[1])
                self.connection.sendall(
                    ("host che contengo i frammenti del file:\n"+stringa).encode())
            elif int(msgR[0]) == 0:
                self.stop()
                '''

    def stop(self):
        self.running = False
    
#esempio menu switch case
while opzione != 0:
    print("\n 1) Verifica se un file è presente nel DB\n",
          "2) Numero di frammenti di un file\n",
          "3) IP di un host che contiene un frammento di un file\n",
          "4) IP di tutti gli host che contengono i frammento di un file\n")

    opzione = int(input("Inserisci l'opzione: "))

    if opzione == 1:
        nomeFile = input("Inserisci il nome del file: ")
        s.sendall(f"{opzione},{nomeFile}".encode())
        msgR = s.recv(4096).decode()
        print(msgR)

#inizializzazione server socket UDP
import socket
#                      IPv4             UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #INET è l'Ipv4
s.bind(("192.168.0.123",5000)) #SOLO SUI SERVER, 5000 è l'indirizzo del processo 

while True:
    dati, ind_client = s.recvfrom(4096) #4096 è la dimensione del buffer di ricezione in byte
    print(f"{dati.decode()} ricevuti da {ind_client}")
    '''stringa = input("Inserisci una stringa: ")
    s.sendto(stringa.encode(), ind_client)
    '''

#inizializzazione client server UDP
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    stringa = input("Inserisci una stringa: ")
    s.sendto(stringa.encode(), ("192.168.0.129", 5000))
