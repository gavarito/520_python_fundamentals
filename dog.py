#!/usr/bin/python3

class Dog():
    '''tentando abstrair um cachorro'''
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.energia = 5
        self.fome = 5

    def andar(self):
        self.energia -= 1
        self.fome -= 1
        print('''
    andando .... 
    energia: {}
    fome: {}'''.format(self.energia, self.fome))
    def comer(self):
        self.fome = 5
        print('comendo ....')
    
    def dormir(self):
        self.energia = 5
        print('dormindo ....')
    def __str__(self):
        return "nome: {} idade: {} raça: {}".format(self.nome, self.idade, self.raca)

dog1 = Dog('bilu', 2, 'pitbul')
dog2 = Dog('rex', 1, 'poodle')

print(dog1.nome)
dog1.comer()
dog1.dormir()
dog1.andar()
dog1.andar()
dog1.andar()