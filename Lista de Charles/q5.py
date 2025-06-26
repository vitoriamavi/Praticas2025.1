'''Questão 05 (10 pontos)
Faça um programa que receba duas strings compostas por 0 e 1 apenas. Essas strings correspondem a uma sequência binária e devem ter o mesmo comprimento.
Pede-se que, após a leitura e a validação das duas strings, o programa apresente o resultado das operações lógicas AND, OR e XOR entre essas duas variáveis.'''

verifica = 0
string1 = ""
string2 = ""

while verifica == 0:
    string1 = (input("Digite a primeira string composta apenas por 0 e 1: "))
    string2 = (input("Digite a segunda string composta apenas por 0 e 1: "))
    
    validoString1 = 1 # valida para a primeira string
    for digito in string1:
        if digito != '0' and digito != '1':
            validoString1 = 0
            break # sai do for quando encontra um digito inválido

    validoString2 = 1 # valida para a segunda string
    for digito in string2:
        if digito != '0' and digito != '1':
            validoString2 = 0
            break # sai do for quando encontra um digito inválido

    if validoString1 == 0 or validoString2 == 0: #loop continua enquanto verifica = 0
        print("As sequências devem conter apenas 0 ou 1.")
    elif len(string1) != len(string2):
        print("As sequências devem ter o mesmo comprimento.")
    else:
        verifica = 1 #sai do while

resultAND = ""
resultOR = ""
resultXOR = ""
for i in range(len(string1)):
    bit1 = int(string1[i])
    bit2 = int(string2[i])

    resultAND += str(bit1 & bit2)
    resultOR += str(bit1 | bit2)
    resultXOR += str(bit1 ^ bit2)

print(f"AND: {resultAND}")
print(f"OR: {resultOR}")
print(f"XOR: {resultXOR}")