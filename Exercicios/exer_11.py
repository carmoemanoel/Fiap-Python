import math

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# Calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))