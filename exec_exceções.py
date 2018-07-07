#!/usr/bin/python3

nome = input('Digite o nome do arquivo: ')
try:
    with open(nome + '.txt', 'r') as arquivo:
       conteudo = arquivo.readlines()
       print(conteudo)

except FileNotFoundError as e:
    print('Arquivo não existe')
finally:
    print('sempre executa')