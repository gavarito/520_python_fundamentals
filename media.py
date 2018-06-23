#!/usr/bin/python3

nome = input('Digite seu nome: ')
nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))

soma_notas = nota1 + nota2
media = float(soma_notas / 2)

print('O aluno {0} tem a media {1}'.format(nome.title(), media))