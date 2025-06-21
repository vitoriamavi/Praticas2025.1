'''Existem somente quatro números, maiores do que um, que podem ser obtidos pela soma de potências de 4 dos seus dígitos:
1643 = 1⁴ + 6⁴ + 4⁴ + 3⁴
8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
Faça um programa que encontra e exibe os números menores de 1.000.000, que são múltiplos de 2 ou 5 e que podem ser escritos pela soma das potências de 5 de seus dígitos.'''

for numero in range(2, 1000000):
    if numero % 2 == 0 or numero % 5 == 0:
        soma = 0
        temp = numero
        explicacao = ""
        contador = 0

        while temp > 0:
            digito = temp % 10
            potencia = digito ** 5
            soma += potencia
            termo = str(digito) + "^5 = " + str(potencia)
            if contador == 0:
                explicacao = termo
            else:
                explicacao = termo + " + " + explicacao
            temp //= 10
            contador += 1

        if soma == numero:
            print("Número encontrado: " + str(numero))
            print("Componentes da soma:")
            print(explicacao)
            print("-" * 40)