#!/usr/bin/python3
def externa(idioma):
    dic = {'pt': 'Ola', 'pi':'Ahoy', 'en': 'Hello'}
    def interna(nome):
        print('{} {}'.format(dic[idioma], nome))
    return interna

func = externa('pi')
func('Joseph')
func('Daniel')
func('Joao')