#!/usr/bin/python3

from dog import Dog
from time import sleep

dog1 = Dog('bilu', 2, 'pitbul')
dog2 = Dog('rex', 1, 'poodle')

print(dog1.__doc__)

exit()
while True:
    if dog1.energia > 0 and dog1.fome > 0:
        dog1.andar()
    if dog1.energia == 0:
        dog1.dormir()
        sleep(1)
    if dog1.fome == 0:
        dog1.comer()
        sleep(1)
    sleep(2)

# print(dog1.nome)
# dog1.andar()
# dog1.andar()
# dog1.comer()
# dog1.andar()