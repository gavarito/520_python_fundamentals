#!/usr/bin/python3

from car import Car, Carro_eletrico
from time import sleep

carro1 = Car('Fiat', 'Uno', 1998)
carro2 = Carro_eletrico('Prius', 'Toyota', 2018)
print(carro1.combustivel)
print(carro2.tanque)

exit()
while True:
    if carro1.tanque > 0 and carro1.motor > 0:
        carro1.andar()
    if carro1.tanque == 0:
        litros = int(input('Quantos litros quer abastecer? '))
        carro1.abastercer(litros)
        sleep(1)
    elif carro1.motor == 0:
        carro1.revisao()
        sleep(1)
    sleep(2)