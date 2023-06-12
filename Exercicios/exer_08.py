# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com um desconto de 5%.


produto = float(input('Digite o preço do produto: '))

porcentagem  = 5/100

des =  produto * porcentagem

total = produto - des

print('O valor do produto é {} e com o desconto de 5% passa a ser {}'.format(produto, total))