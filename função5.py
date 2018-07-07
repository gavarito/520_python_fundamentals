#!/usr/bin/python3

def boas_vindas(**kwargs):
    for x, y in kwargs.items(): #.values .keys .items
        print(x, y, sep=':')

boas_vindas(nome='joseph', sobrenome='prata', idade=24)