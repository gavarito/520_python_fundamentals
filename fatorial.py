#!/usr/bin/python3
def factorial(num):
    aux = 1
    for x in range(1,num+1):
        aux *= x
    return aux


# from math import factorial

num = int(input('Digite o número: '))
print(factorial(num))