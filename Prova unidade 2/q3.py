def contar_palavras(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        e = arquivo.read()
        palavras = e.split()
        qtdpalavras = len(palavras)
    print(f"O arquivo {nomeArquivo}, contém {qtdpalavras} palavras")
nomeArquivo = input("nome?")