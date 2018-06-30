#!/usr/bin/python3
par = []
impar = []
for x in range(10):
    num = int(input('Digite o numero: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(par)
print(impar)