#!/usr/bin/python3

nomes = ['joseph', 'joao', 'maria', 'ana']
#nomes = []
#while True:
#    nome = input('Digite um nome ou sair: ')
#    if nome.lower().strip() == 'sair':
#        break
#    nomes.append(nome)

#print(nomes[0])
for pessoa in nomes:
    if pessoa.lower().strip() == 'ana':
        print('achei')
        break
else:
    print('nao achei a ana')