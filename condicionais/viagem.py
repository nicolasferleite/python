distancia = int(input('Digite a distancia percorrida: '))
if(distancia <= 200):
    passagem = distancia * 0.5
    print("A sua passagem é R${:.2f}.".format(passagem))
else:
    passagem = distancia * 0.45
    print("A sua passagem é R${:.2f}".format(passagem))