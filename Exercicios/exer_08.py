# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com um desconto de 5%.


produto = float(input('Digite o preço do produto R$'))

des = produto - (produto * 5 / 100)

print('O preço do produto é {} e com o desconto de 5% passa a ser {}'.format(produto, des))