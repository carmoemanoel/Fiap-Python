# Crie um programa que leia o quanto de dinheiro um pessoa tem na carteira e mostre quantos Dólares
# ela pode comprar;

# Obs: Usar a cotação atual.

numero = float(input('Digite uma quantia em reais para comprar Dólar: '))

cotaçãoDolar = numero / 4.88

print('A quantia de R$ {} consegue comprar {:2f} em Dólar.'.format(numero, cotaçãoDolar))