import sqlite3

id = 1
nome = "dune.mov"
con = sqlite3.connect("./file.db")
cur = con.cursor()
res = cur.execute(f"SELECT nome FROM files")
s= res.fetchall()

for lettere in s:
    if lettere[0] == nome:
        print("corretto")
        break
print(s)
con.close()