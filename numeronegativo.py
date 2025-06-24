soma = 0
q = 0
nums = []

n = int(input("Digite um número: "))
while n > 0:

    soma += n
    q += 1
    nums.append(n)

    n = int(input("Digite um número: "))

if q > 0:
    media = soma / q
    soma = 0
    for n in nums:
        soma += (n - media)**2
    variancia = soma / q
    print(f"A média é {media} e a variância é {variancia}")