import string

def ler_arquivo(nome_arquivo):
    conteudo_completo = ""
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                conteudo_completo += linha.strip() + " "
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return conteudo_completo.strip()

def forca_bruta(mensagem):
    if len(mensagem) == 1:
        return [mensagem]

    combinacoes = []
    for i in range(len(mensagem)):
        char_atual = mensagem[i]
        resto = mensagem[:i] + mensagem[i+1:]
        for p in forca_bruta(resto):
            combinacoes.append(char_atual + p)
    return combinacoes

def rodar_letra(letra, numero):
    if letra == '#':
        return ' '

    alfabeto = string.ascii_lowercase
    tamanho_alfabeto = len(alfabeto)

    if letra not in alfabeto:
        return letra

    indice_inicial = alfabeto.index(letra)
    indice_novo = (indice_inicial - numero) % tamanho_alfabeto
    return alfabeto[indice_novo]

def aplicar_todas_as_rotacoes(vetor_combinacoes):
    resultado_final = []
    for combinacao in vetor_combinacoes:
        tamanho = len(combinacao)
        rotacoes_combinacao = []

        for n in range(tamanho):
            nova_combinacao = ''.join(rodar_letra(letra, n) for letra in combinacao)
            rotacoes_combinacao.append(nova_combinacao)

        resultado_final.append(rotacoes_combinacao)
    return resultado_final

arquivo_mensagem_criptografada = 'mensagem_criptografada.txt'
mensagem_criptografada = ler_arquivo(arquivo_mensagem_criptografada)

possibilidades = forca_bruta(mensagem_criptografada)

resultado = aplicar_todas_as_rotacoes(possibilidades)

with open("combinacoes.txt", "w") as file:
    for combinacao in resultado:
        for conteudo in combinacao:
            file.write(f"{conteudo}\n")