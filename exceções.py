#!/usr/bin/python3

try:
    num = int(input('Digite um número inteiro: '))
    num1 = int(input('Digite um numero inteiro: '))
    div = num / num1
    print(div)
except ValueError as e:
    print('não é um número {}'.format(e))
except ZeroDivisionError as e:
    print('erro de divisão por 0 {}'.format(e))
except KeyboardInterrupt as e:
    print('adeus...')
except Exception as e:
    print('erro')

#print(num)