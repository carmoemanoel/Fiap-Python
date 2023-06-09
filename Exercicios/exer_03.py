# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = int(input('Digite a sua primeira nota: '))
nota2 = int(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

print('A primeira nota foi {} e a segunda nota foi {} e a média é {}.'.format(nota1, nota2, media))