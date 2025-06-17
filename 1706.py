import random
palavras = ("abacate", "lima", "abacaxi")

segredo = palavras [random.randint(0,2)]

visivel = "-" * len(segredo)

tentativas = 0

while visivel != segredo:
    print (visivel)
    
    letra = input("Digite uma letra: ")
    novavisivel = ""
    
    for pos in range(len(segredo)):
        if letra != segredo[pos]:
            novavisivel += visivel[pos]
        else:
            novavisivel += segredo[pos]
    visivel = novavisivel
if visivel == segredo:
    print (segredo)