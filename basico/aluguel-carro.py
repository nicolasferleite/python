dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros o carro percorreu? '))
print('O total a pagar pelo aluguel do carro é: R${:.2f}'.format((60*dias) +(0.15*km)))