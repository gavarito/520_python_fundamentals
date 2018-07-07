#!/usr/bin/python3

def decorador(func):
    def interna(x, y):
        print(x, y)
    return interna