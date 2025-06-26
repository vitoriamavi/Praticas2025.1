'''Questão 05 (10 pontos)
Faça um programa que receba duas strings compostas por 0 e 1 apenas. Essas strings correspondem a uma sequência binária e devem ter o mesmo comprimento.
Pede-se que, após a leitura e a validação das duas strings, o programa apresente o resultado das operações lógicas AND, OR e XOR entre essas duas variáveis.'''

verifica = 0
string1 = ""
string2 = ""

while verifica == 0:
    string1 = (input("Digite a primeira string composta apenas por 0 e 1: "))
    string2 = (input("Digite a segunda string composta apenas por 0 e 1: "))
    
    validoString1 = 1 #valida para a primeira string
    for digito in string1:
        if digito != 0 and digito != 1:
            validoString1 = 0
            break #sai do loop quando encontra um digito inválido

    validoString2 = 1 #valida para a primeira string
    for digito in string2:
        if digito != 0 and digito != 1:
            validoString2 = 0
            break #sai do loop quando encontra um digito inválido

    if validoString1 == 0 or validoString2 == 0:
        print("As sequências devem conter apenas 0 ou 1.")

    elif len(string1) != len(string2):
        print("As sequências devem ter o mesmo comprimento")
    
    else:
        verifica = 1

and = ""
or = ""
xor = ""


