'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados
Ex: 
Digite um número: 1834
Unidade:4
dezena:3
centena:8
milhar:1 
'''

num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))