import random
palavras = ("ABACATE", "LIMA", "ABACAXI")

segredo = palavras [random.randint(0,len(palavras)-1)]

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
    print ("Você acertou! a palavra era:", segredo)
else:
    print ("Você errou! a palavra era:", segredo)