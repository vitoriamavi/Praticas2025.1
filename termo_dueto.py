import random

# Lista de palavras (só como exemplo)
palavras = ["nuvem", "livro", "praia", "festa", "sabre", "tempo"]

# Selecionar duas palavras aleatórias
resposta1, resposta2 = random.sample(palavras, 2)

tentativas = 6
print("Bem-vinda ao Termo Dueto! Tente adivinhar as duas palavras.")

while tentativas > 0:
    palpite1 = input("Palpite 1: ").upper()
    palpite2 = input("Palpite 2: ").upper()
    
    acertos = 0
    if palpite1 == resposta1 or palpite1 == resposta2:
        print("Você acertou uma palavra!")
        acertos += 1
    if palpite2 == resposta1 or palpite2 == resposta2:
        print("Você acertou outra palavra!")
        acertos += 1

    if acertos == 2:
        print("Parabéns! Você acertou as duas palavras!")
        break

    tentativas -= 1
    print(f"Restam {tentativas} tentativas.")

if tentativas == 0:
    print(f"As palavras eram: {resposta1} e {resposta2}")