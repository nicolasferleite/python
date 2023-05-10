n1 = int(input('Digite o valor da primeira reta: '))
n2 = int(input('Digite o valor da segunda reta: '))
n3 = int(input('Digite o valor da terceira reta: '))

if(n1 + n2 > n3 or n2 + n3 > n1 or n1 + n3 > n2):
    print("É possivel formar um triangulo.")
else:
    print("Nao é possivel formar um triangulo.")