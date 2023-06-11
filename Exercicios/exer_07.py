# Programa que lê a  altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta 
# necessária para pinta-la, sabendo que cada litro de tinta pinta um área de 2m2

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
litrosTinta = area / 2

print('A área total da parede é {} metros e é necessário {} litros de tinta para pintar a parede.'.format(area, litrosTinta))

