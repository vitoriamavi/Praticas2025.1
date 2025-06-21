'''Questão 01 (05 pontos)
Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Faça um programa que solicite a massa inicial (em gramas) e que calcule o tempo necessário para que essa massa se torne menor que 0,5 grama. Ao término, o programa deve exibir a massa inicial, a massa final e o tempo que levou para o decaimento (exiba o tempo informando horas, minutos e segundos).
Exemplo de saída:
Massa Inicial: 250 gramas
Massa Final: 0.48828125 gramas
Tempo de Decaimento: 0:07:30'''

massaInicial = float(input("Digie a massa inicial do material radioativo: "))
tempoEmSegundos = 0

while massaInicial >=  0.5:
    massa /= 2
    tempoEmSegundos += 50

horas = tempoEmSegundos//3600
minutos = (tempoEmSegundos % 3600) //60
segundos = tempoEmSegundos % 60

print(f"Massa inicial: {massaInicial} gramas.")
print(f"Massa Final: {massa} gramas")
print(f"Tempo de Decaimento: {int(horas):02d}:{int(minutos):02d}:{int(segundos):02d}")