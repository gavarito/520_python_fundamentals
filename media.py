#!/usr/bin/python3

nome = input('Digite seu nome: ')
soma = 0
for x in range(4):
    nota = int(input('Digite a nota {}: '.format(x+1)))
    soma += nota
media = soma / 4

if media >=7:
    result = 'aprovado'
else:
    result = 'reprovado'
    
print('O aluno {} tem a media {}, ele esta {}!'.format(nome.title(), media, result))