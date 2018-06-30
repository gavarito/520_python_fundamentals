#!/usr/bin/python3

with open('frutas.txt', 'a') as arquivo:
   arquivo.write('damasco\n')


exit()


#abrir
arquivo = open('frutas.txt', 'r')

#ler o arquivo
print(arquivo.read())

#fechar
arquivo.close()