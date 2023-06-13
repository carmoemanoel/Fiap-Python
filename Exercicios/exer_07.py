# Programa que lê a  altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta 
# necessária para pinta-la, sabendo que cada litro de tinta pinta um área de 2m2

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m.'.format(altura, largura, area))

litrosTinta = area / 2

print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(litrosTinta))

