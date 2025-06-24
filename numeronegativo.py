soma = 0
q = 0
nums = []

n = int(input("Digite um número: "))
while n >= 0:

    soma += n
    q += 1
    nums.append(n)

    n = int(input("Digite um número: "))

if q > 0:
    media = soma / q
print(media)