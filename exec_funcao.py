#!/usr/bin/python3

def valor_vendas(**produto):
    a = produto['qtd']
    b = produto['preco']
    c = produto['nome']
    result = 'produto: {}, Total: {}'.format(c, a * b)
    return result
        


print(valor_vendas(nome='abacaxi', qtd=8, preco=5.00))