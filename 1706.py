import random
palavras = ("abacate", "lima", "abacaxi")

segredo = palavras [random.randint(0,2)]

visivel = "-" * len(segredo)

tentativas = 0

while visivel != segredo:
    print (visivel)
    
    letra = input("Digite uma letra: ")
    novavisual = ""
    
    for pos in range(len(segredo)):
        if letra != segredo[pos]:
            novavisual += visivel[pos]
        else:
            novavisual += segredo[pos]
    visivel = novavisual
if visivel == segredo:
    print (segredo)