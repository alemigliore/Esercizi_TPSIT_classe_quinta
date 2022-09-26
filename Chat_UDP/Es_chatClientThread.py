import socket
from threading import Thread

sClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sServer.bind(("0.0.0.0", 5000))

class receive(Thread):
    def __init__(self):   
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            msg, ind_client = sServer.recvfrom(4096)
            print(msg.decode()) 

    def stop(self):
        self.running = False

def main():
    r = receive()
    r.start()

    while True:
        messaggio = input("Inserisci il messaggio: ")
        nick = input("Inserisci il nickname del destinatario: ")
        string = messaggio + "|" + nick
        sClient.sendto(string.encode(), ("192.168.0.136", 5000))
        if messaggio == "break":
            r.stop()
            r.join()
            break

    sClient.close()
    
if __name__ == "__main__":
    main()

#cd Documents\scuola\sistemi\Quinta_superiore\python\reteServerClient\Chat