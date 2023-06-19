# O mesmo professor do desafio anterior quer sortear a ordem de apresentação do trabalho dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada embaralhada.

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1 , n2, n3, n4]

random.shuffle(lista)
print('A ordem de apresentação será...')
print(lista)