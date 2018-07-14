#!/usr/bin/python3

try:
    ling = input('Qual a melhor linguagem? ')
    if ling == 'python':
        print('Você acertou!')
    else:
        raise TypeError
except TypeError as e:
    print('erro tipo invalido')
finally:
    print('sempre executa')