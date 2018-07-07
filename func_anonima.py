#!/usr/bin/python3

from func_abre_arq import abre_arquivo
from random import choice

pessoas = abre_arquivo('nomes.txt', 'r')
pessoa = choice(pessoas)
print(pessoa)

funcoes = [
    lambda nome: nome.title(),
    lambda nome: nome.upper(),
    lambda nome: nome.lower(),
    lambda nome: nome.replace('a', '@'),
]
for x in funcoes:
    print(x(pessoa), end='')




# nomes = ('joseph', 'iza', 'jessica')
# choice(nomes)
# print(choice(nomes))


exit()
lista = [
    lambda x,y: x + y,
    lambda x,y: x - y,
    lambda x,y: x * y,
    lambda x,y: x ** y,
    lambda x,y: x ** 0.5 + y ** 0.5
]

for item in lista:
    print(item(64,25))

exit()
potencia = lambda x,y: x ** y
print(potencia(2,10))

exit()
var = lambda x,y: x + y

print(var(10,5))