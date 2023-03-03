import socket,sqlite3
from threading import Thread
listaThread = []
class myThread(Thread):
    def __init__(self,s,connection):
        Thread.__init__(self)
        self.s = s
        self.connection = connection
        self.running = True
    def run(self):
        con = sqlite3.connect("./file.db")
        cur = con.cursor()
        while self.running:
            dati = self.connection.recv(4096).decode()
            print(dati)
            divisi = dati.split(",")
            if dati.lower() == "exit": break
            if divisi[0] == "1":
                res = cur.execute(f"SELECT nome FROM files WHERE files.nome = {divisi[1]}")
                if res.fetchone(): 
                    self.connection.sendall("il file richiesto è presente nel db".encode())
            if divisi[0] == "2":
                res = cur.execute(f"SELECT tot_frammenti from files where files.nome = {divisi[1]}")
                if res.fetchone(): 
                    self.connection.sendall(f"il file richiesto ha {res} frammenti".encode())
            if divisi[0] == "3":
                res = cur.execute(f"SELECT host from files,frammenti where nome = {divisi[1]} and n_frammento = {int(divisi[2])} and files.id_file = frammenti.id_file")
                if res.fetchone():
                    self.connection.sendall(f"l' host è {res}".encode())
            if divisi[0] == "4":
                res = cur.execute(f"SELECT host from files,frammenti where nome = {divisi[1]} and files.id_file = frammenti.id_file")
                elenco = "".join(str(cella) + " " for cella in res.fetchall())
                print(elenco)
                self.connection.sendall(f"elenco: {elenco}".encode())
    def stop(self):
        self.running = False

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("127.0.0.1",5000))
    s.listen()
    while True:
        connection,_ = s.accept()
        listaThread.append(myThread(s, connection))
        listaThread[len(listaThread)-1].start()


if __name__ == "__main__":
    main()