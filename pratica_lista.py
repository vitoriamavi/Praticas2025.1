n = int(input("Digite um número: "))
nums = []
tamanho = 0

while n > 0:
    nums.append (n)
    tamanho += 1
    n = int(input("Digite um número: "))

print(f"O tamanho da lista é {tamanho}")

numero = int(input("Digite um número: "))

aparece = 0

for a in nums:
    if a == numero:
        aparece += 1
print(f"O número aparece {aparece} vezes")
