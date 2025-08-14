def valida_luhn(num_cartao: str) -> bool:
    if len(num_cartao) != 16 or not num_cartao.isdigit():
        return False
    soma = 0
    for i in range(16):
        n = int(num_cartao)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
    return soma % 10 == 0
num_cartao = int(input("Digite o número do cartão: "))
if valida_luhn:
    print("Cartão válido!")
else:
    print("Cartão inválido!") 
