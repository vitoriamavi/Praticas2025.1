soma = 0
q = 0

n = int(input("Digite um número: "))
while n >= 0:

    soma += n
    q += 1

    n = int(input("Digite um número: "))

if q > 0:
    media = soma / q
print(media)