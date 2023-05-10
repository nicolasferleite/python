from random import randint
n = randint(0,5)
chute = int(input('Tente adivinhar o numero escolhido: '))
if(chute == n):
    print("Você acertou!")
else:
    print("Você errou! O numero escolhido foi {}.".format(n))