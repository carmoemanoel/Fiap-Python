# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
sqrt = numero ** (1/2)

print('O numero digitado foi {} e o seu dobro é {}, seu triplo {} e a sua raiz quadrada é {}.'.format(numero, dobro, triplo, sqrt))