import math

# Criar um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: O número digitado 6.127 e a sua parte inteira 6

num = float(input('Digite um número real para mostrarmos a sua porção inteira: '))

print('O número digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
