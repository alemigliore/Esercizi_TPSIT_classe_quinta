import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",5000))
    while True:
        print("1)chiedere al server se un certo nome file è presente\n2)chiedere al server il numero di frammenti di un file a partire dal suo nome file;\n3)chiedere al server l’IP dell’host che ospita un frammento a partire nome file e dal numero del frammento;\n4)chiedere al server tutti gli IP degli host sui quali sono salvati i frammenti di un file a partire dal nome file.")
        domanda = int(input("fai la tua scelta: "))
        if domanda in [1,2,3,4]:
            nomeFile = input("inserisci un nome file: ")
        if domanda in [1,2,4]:
            s.sendall(f"{str(domanda)},{nomeFile}".encode())
        if domanda == 3:
            n_frammento = int(input("inserisci in numero di frammenti: "))
            s.sendall(f"{str(domanda)},{nomeFile},{str(n_frammento)}".encode())
        dati = s.recv(4096).decode()
        print(dati)

if __name__ == "__main__":
    main()