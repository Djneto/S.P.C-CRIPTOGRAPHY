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

def rodar_alfabeto(indice, letra):
    alfabeto = string.ascii_lowercase
    tamanho_alfabeto = len(alfabeto)

    if letra not in alfabeto:
        raise ValueError("A letra fornecida não está no alfabeto.")

    indice_inicial = alfabeto.index(letra)
    indice_rodado = (indice_inicial - indice) % tamanho_alfabeto

    return alfabeto[indice_rodado]

def descriptografar(chave, mensagem_criptografada):
    chave_lista = list(map(int, chave.split()))
    mensagem_reordenada = ''

    for i in range(len(chave_lista)):
        mensagem_reordenada += mensagem_criptografada[chave_lista.index(i)]

    conteudo_descriptografado = ''

    for letra in mensagem_reordenada:
        if letra == '#':
            conteudo_descriptografado += ' '
        else:
            conteudo_descriptografado += rodar_alfabeto(int(chave_lista[0]), letra)

    with open('mensagem_descriptografada.txt', 'w') as arquivo:
        arquivo.write(conteudo_descriptografado)

arquivo_mensagem_criptografada = 'mensagem_criptografada.txt'
arquivo_chave = 'chave.txt'

chave = ler_arquivo(arquivo_chave)
mensagem_criptografada = ler_arquivo(arquivo_mensagem_criptografada)

descriptografar(chave, mensagem_criptografada)