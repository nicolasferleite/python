velocidade = int(input('Digite a velocidade com qual vc estava dirigindo: '))
if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print("Voce excedeu a velocidade limite, portanto vc devera pagar uma multa de R${}.".format(multa))
else:
    print("Parabens! Vc esta dentro da velocidade permitida.")