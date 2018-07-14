#!/usr/bin/python3

try:
    arq = input('Digite o nome de um arquivo: ')
    if arq == 'privado':
        raise FileNotFoundError
    else:
        with open(arq, 'r') as arquivo:
            conteudo = arquivo.readlines()
            print(conteudo)
except FileNotFoundError as e:
    print('Arquivo inexistente!')

