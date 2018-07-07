#!/usr/bin/python3
from datetime import datetime

def abre_arquivo(nome, modo, conteudo=None):
    if modo == 'r':
        try:
            with open(nome, modo) as arquivo:
                return arquivo.readlines()
        except Exception as e:
            return 'Falha ao ler o arquivo {}!'.format(e)
    elif modo == 'a':
        try:
            with open(nome, modo) as arquivo:
                arquivo.write(conteudo)
                return abre_arquivo(nome, 'r')
        except Exception as e:
            return 'Falha ao ler o arquivo {}!'.format(e)

print(abre_arquivo('frutas.txt', 'a', 'inga\n'))

# nome = input('Digite o nome do arquivo: ')
# print(abre_arquivo(nome + '.txt'))