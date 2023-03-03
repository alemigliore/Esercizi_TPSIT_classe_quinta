import socket
import alphabot
import time
import sqlite3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot = alphabot.AlphaBot()
comandi = {"w":bot.forward, "a":bot.left, "d":bot.right, "s":bot.backward, "q":bot.stop}
s.bind(("0.0.0.0", 8000))
s.listen()
print("In attesa di connessione...")
connection, address = s.accept()


while True:
    msgR = connection.recv(4096)
    msgR = msgR.decode()

    if(len(msgR) != 1):
        ls = msgR.split(" ")
        tempo = float(ls[1])
    else:
        ls = msgR
    """else:
        id = msgR
        con = sqlite3.connect("./movimenti.db")
        cur = con.cursor()
        res = cur.execute(f"SELECT Movimento FROM Movimento WHERE ID = {id}")
        move = res.fetchall()
        print(move)
        move = move[0][0]
        print(move)

        lista = move.split(";")
        for comando in lista:
            msg = comando.split("|")
            ls[0] = msg[0]
            tempo = float(msg[1])"""
    

    if(ls[0] == "w"):
        bot.forward()
        time.sleep(tempo)
        bot.stop()
    elif(ls[0] == "a"):
        bot.left()
        time.sleep(tempo)
        bot.stop()
    elif(ls[0] == "d"):
        bot.right()
        time.sleep(tempo)
        bot.stop()
    elif(ls[0] == "s"):
        bot.backward()
        time.sleep(tempo)
        bot.stop()
    elif(ls[0] == "q"):
        bot.stop()
    elif(ls[0] == "1"):
        bot.forward()
        time.sleep(2.2)
        bot.right()
        time.sleep(0.15)
        bot.forward()
        time.sleep(4)
        bot.right()
        time.sleep(0.18)
        bot.stop()
    elif(ls[0] == "2"):
        bot.forward()
        time.sleep(2.2)
        bot.left()
        time.sleep(0.23)
        bot.forward()
        time.sleep(2.2)
        bot.stop()
    elif(ls[0] == "3"):
        bot.forward()
        time.sleep(2.4)
        bot.right()
        time.sleep(0.15)
        bot.forward()
        time.sleep(1.9)
        bot.right()
        time.sleep(0.15)
        bot.forward()
        time.sleep(2.2)
        bot.right()
        time.sleep(0.15)
        bot.forward()
        time.sleep(2.2)
        bot.stop()
    elif(ls[0] == "4"):
        bot.forward()
        time.sleep(3)
        bot.left()
        time.sleep(0.28)
        bot.forward()
        time.sleep(3)
        bot.left()
        time.sleep(0.28)
        bot.forward()
        time.sleep(3)
        bot.left()
        time.sleep(0.28)
        bot.forward()
        time.sleep(3)
        bot.stop()
    s.close()
