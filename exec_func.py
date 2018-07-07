#!/usr/bin/python3

from datetime import datetime
from func_abre_arq import abre_arquivo

while True:
    nome_arq = input('Digite o nome do arquivo ou s para sair: ')
    if nome_arq == 's':
        break
    mod = input('Modo de abertura: ')
    if mod == 'r':
        a = abre_arquivo(nome_arq, mod)
        print(a)
    elif mod == 'a':
        conteudo = input('Digite o conteudo: ')
        abre_arquivo(nome_arq, mod, conteudo + '\n')
