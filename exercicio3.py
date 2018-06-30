#!/usr/bin/python3
with open('nomes.txt', 'w') as arquivo:
    while True:
        nome = input('Digite um nome ou sair: ')
        if nome.lower().strip() == 'sair':
            break
        arquivo.write(nome + '\n')

with open('nomes.txt', 'r') as arquivo:
    print(arquivo.readlines())
        
