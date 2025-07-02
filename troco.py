conta = int(input("Valor da conta (R$): "))
pago = int(input("Valor pago (R$): "))
troco = pago - conta
print(f"Troco: R$ {troco}") 

if troco > 0:
    print("\nCédulas:")
    notas = [200, 100, 50, 20, 10, 5, 2]
    for nota in notas:
        quantidade = troco // nota
        if quantidade > 0: print(f"- {quantidade} cédula(s) de R$ {nota:.0f}")
        troco %= nota