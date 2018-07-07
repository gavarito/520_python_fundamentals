#!/usr/bin/python3

def boas_vindas(*args):
    for x in args:
        print('Seja bem vindo(a) {}'.format(x))

nomes = ['joseph', 'iza', 'jessica']
boas_vindas(nomes)