conta = int(input("Valor da conta: "))
pago = int(input("Valor pago: "))
troco = pago - conta
print(f"Troco: R$ {troco}") 
notas = [200, 100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = troco // nota
    if quantidade > 0: print(f"{quantidade} cédula(s) de R$ {nota}")
    troco %= nota