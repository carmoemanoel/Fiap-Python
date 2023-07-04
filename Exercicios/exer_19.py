'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes apareceu a letra 'A';
- Em que posição ela aparece pela primeira vez;
- Em que posição ela aparece pela última vez;
'''

frase = input('Digite uma frase:')
print('A letra'+' A '+'apareceu',frase.count('a'))
print('A letra'+' A '+'apareceu pela primeira vez na posição', frase.find('a'))
 