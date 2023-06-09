# Escrever um programa que leia um valor em metros e exiba na tela convertido em centímetros e depois em milímetros

numero = int(input('Digite um valor para calcular: '))

cent = numero * 100
mil = numero * 1000

print('O número digitado em metros foi {}m e em centímetros são {}cm e em milímetros é {}mil.'.format(numero, cent, mil))