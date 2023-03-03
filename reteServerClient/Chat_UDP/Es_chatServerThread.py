import socket
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(("0.0.0.0",5000))

    f = open(".\File.csv", "r")
    righe = f.readlines()
    f.close()
    contatti = {}
    for riga in righe:
        persona = riga.split(",")
        nome = str(persona[0])
        indirizzo = str(persona[1][:-1])
        contatti[nome] = indirizzo
    print(contatti)


    while True:
        msg, ind_client = s.recvfrom(4096)
        print(f"{msg.decode()} inviati da {ind_client[1]}")
        msgDiviso = msg.decode().split("|")
        print(msgDiviso)
        msgFinale = msgDiviso[0] 
        ip = contatti[msgDiviso[1]]

        s.sendto(msgFinale.encode(),(ip,5000))