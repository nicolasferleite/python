altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largura da parede: '))
area = altura*largura
print('A area dessa parede eh igual a {} metros.'.format(area))
print('Voce ira precisar de {:.0f} litros de tinta para pintar a parede toda.'.format(area / 2))