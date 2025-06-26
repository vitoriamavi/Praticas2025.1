import random

n = int(input("Digite um número: "))
l = []

for i in range(0, 100):
    l.append(random.randint(n - (n*2), n))
    pares = (filter(lambda x: (x % 2 == 0) and (x >=0), l))

for num in pares:
    print(num, end=",")

print(list(pares))