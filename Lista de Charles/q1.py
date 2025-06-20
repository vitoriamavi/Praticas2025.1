limite = 1000000
i = 0

while i < limite:
    if i % 2 == 0 or i % 5 == 0:
        soma = 0
        for digito in str(i):
            soma += digito **5
        if soma == i:
            print (i)
        i += 1