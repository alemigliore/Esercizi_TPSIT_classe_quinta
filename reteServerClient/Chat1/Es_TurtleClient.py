import socket
from threading import Thread
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

class receive(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            msg, ind_client = s.recvfrom(4096)
            print("Server>" + msg.decode())

    def stop(self):
        self.running = False
    
def main():

    s.sendto("Connesso".encode(),("127.0.0.1",5000))
    r = receive()
    r.start()

    while True:
        msg = input()
        s.sendto(msg.encode(),("127.0.0.1",5000))
        if msg == "break":
            r.stop()
            r.join()
            break
    
if __name__ == "__main__":
    main()