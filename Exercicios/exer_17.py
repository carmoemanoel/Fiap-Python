'''
- Criar um programa que leia um nome completo de uma pessoa e mostre:
* O nome com todas as letras maiusculas;
* O nome com todas as letras minusculas;
* Quantas ao todo o (sem considerar espaços);
* Quantas letras tem o primero nome
'''

nome = input('Digite o seu nome completo em letras minisculas:')
print('O nome com todas as letras em maiusculas eh', nome.upper())
nome = input('Digite o seu nome completo em letras maiusculas:')
print('O nome com todas as letras minisculas eh',nome.lower())
nome = input('Digite o seu nome completo para saber o total de letras:')
print('O total de letras desse nome eh', len(nome.strip()))
nome = input('Digite o seu nome completo:')
dividido = nome.split()
print('A quantidade de letras do primero nome eh',len(dividido[0].strip()))