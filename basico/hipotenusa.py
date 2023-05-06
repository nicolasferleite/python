import math
cat1 = float(input('Digite o valor do primeiro cateto: '))
cat2 = float(input('Digite o valor do segundo cateto: '))
hipotenusa = math.sqrt(pow(cat1,2) + pow(cat2,2))
print('O valor da hipotenusa é {:.2f}' .format(hipotenusa))