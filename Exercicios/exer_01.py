# Fazer um programa que leia um número inteiro e mostre na tela 
# o seu sucessor e o seu antecessor.

numero = int(input('Digite um numero: '))
sucessor = numero + 1
antecessor = numero -1

print('O numero digitado foi {} e o seu sucessor é {} e o seu antecessor é {}.'.format(numero, sucessor, antecessor ))