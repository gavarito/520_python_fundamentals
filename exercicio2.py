#!/usr/bin/python3
from pprint import pprint
frutas = [
    {'tipo':'laranja', 'preco':3.5, 'qtd':10},
    {'tipo':'abacaxi', 'preco':5.5, 'qtd':20},
    {'tipo':'uva', 'preco':4.45, 'qtd':30},
    {'tipo':'pera', 'preco':2.0, 'qtd':18},
]

#total = 0
frutas1 = []
for fruta in frutas:
    #total += fruta['preco'] * fruta['qtd']
    fruta['preco'] += fruta['preco'] * 0.1
    frutas1.append(fruta)
pprint(frutas1)

#print('Total R$ {}'.format(total))
