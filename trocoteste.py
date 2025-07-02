conta = int(input("Valor da conta: ")) #Pede o valor da conta// int-valor digitado
pago = int(input("Valor pago: ")) #Mostra o pagamento feito pela pessoa
troco = pago - conta  #Calcula o valor pago
print("O troco é:", troco) #Mostrar o valor do troco 
cedulas = [100, 50, 20, 10, 5, 2, 1] #Lista com as cedulas que esta disponiveis.

for c in cedulas: #laço de repetição// e o 'c' é a variavel utilizada
    if troco // c > 0: #Pra saber se vai precisa usar uma determida cedula
        print(f"{troco // c}, cédula(s) de R$", c) #Mostra o total de cedulas usadas.
        troco %= c