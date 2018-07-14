#!/usr/bin/python3

class Car():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tanque = 20
        self.motor = 10
        self.combustivel = 'gasolina'

    def andar(self):
        self.tanque -= 2
        self.motor -= 1
        print('''
        Andando...
        Tanque: {}
        Motor: {}'''.format(self.tanque, self.motor))

    def abastercer(self, litros):
        self.tanque += litros
        print('Abastecendo...')

    def revisao(self):
        self.motor = 10
        print('Revisando...')

    def __str__(self):
        return "marca: {} modelo: {} ano: {}".format(self.marca, self.modelo, self.ano)

class Carro_eletrico(Car):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.combustivel = 'energia'

carro1 = Car('Fiat', 'Uno', 1998)
print(carro1)
