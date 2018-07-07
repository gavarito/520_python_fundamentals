#!/usr/bin/python3
from math import pi, pow
raio = int(input('Digite o raio do circulo: '))
area = pi * pow(raio, 2)

print('A area do circulo é {:.2f}'.format(area))