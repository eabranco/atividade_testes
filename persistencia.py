def salvar_pontuacao(nome, pontos):
    with open("pontuacoes.txt", "a") as arquivo:
        arquivo.write(f"{nome},{pontos}\n")

def ler_pontuacoes():
    pontuacoes = []
    try:
        with open("pontuacoes.txt", "r") as arquivo:
            for linha in arquivo:
                nome, pontos = linha.strip().split(",")
                pontuacoes.append((nome, int(pontos)))
    except FileNotFoundError:
        print("Arquivo 'pontuacoes.txt' não encontrado. Nenhuma pontuação salva ainda.")
    return pontuacoes