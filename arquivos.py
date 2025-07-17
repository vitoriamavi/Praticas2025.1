fd = open("dados1.txt", "r", encoding="utf-8")
dados = fd.read()
print(dados)
fd.close()