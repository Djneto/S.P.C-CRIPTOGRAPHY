import string
import random

def gerar_chave_aleatoria(tamanho, nome_arquivo):
    chave = list(range(tamanho))
    random.shuffle(chave)
    chave_string = ' '.join(map(str, chave))

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(chave_string)
    return chave

def ler_arquivo_para_string(nome_arquivo):
    conteudo_completo = ""
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                conteudo_completo += linha.strip() + " "
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return conteudo_completo.strip()

def rodar_alfabeto(indice, letra):
    alfabeto = string.ascii_lowercase
    tamanho_alfabeto = len(alfabeto)

    if letra not in alfabeto:
        raise ValueError("A letra fornecida não está no alfabeto.")

    indice_inicial = alfabeto.index(letra)
    indice_rodado = (indice_inicial + indice) % tamanho_alfabeto

    return alfabeto[indice_rodado]

def criptografar(chave, conteudo):
    conteudo_criptografado = ''

    for indice, letra in enumerate(conteudo):
        if letra == ' ':
            conteudo_criptografado += '#'
        else:
            conteudo_criptografado += rodar_alfabeto(chave[0], letra)

    conteudo_reordenado_list = list(conteudo_criptografado)
    for indice, numero in enumerate(chave):
        if indice < len(conteudo_criptografado):
            conteudo_reordenado_list[indice] = conteudo_criptografado[numero]

    conteudo_reordenado = ''.join(conteudo_reordenado_list)

    with open('mensagem_criptografada.txt', 'w') as arquivo:
        arquivo.write(conteudo_reordenado)

    return conteudo_reordenado

arquivo_mensagem = 'mensagem.txt'
arquivo_chave = 'chave.txt'

conteudo = ler_arquivo_para_string(arquivo_mensagem)

tamanho_string = len(conteudo)
chave_aleatoria = gerar_chave_aleatoria(tamanho_string, arquivo_chave)

conteudo_criptografado = criptografar(chave_aleatoria, conteudo)