# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento;

salario = float(input('Digite o preço do Salário: '))

porcentagem  = 15/100

des =  salario * porcentagem

reajuste = salario + des

print('O salário atual é {} e teve um reajuste de 15% passou a ser {}'.format(salario, reajuste))