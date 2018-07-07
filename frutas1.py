#!/usr/bin/python3
#!/usr/bin/python3
with open('frutas.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

with open('frutas1.txt', 'w') as arquivo:
    cont = 1
    for linha in conteudo:
        print(linha.replace('\n', '-{}\n'.format(cont)))
        #arquivo.write(linha)
        cont += 1