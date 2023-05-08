frase = "Nicolas Ferreira Leite"
print(frase[0:7]) #ler do caractere 0 ao 6, n conta o 7 pois para 1 antes
print(frase[8:16])
print(frase[17:22])
print(len(frase)) #ler a quantidade de caracteres da frase
print(len(frase[0:7]))
print(frase.count('e')) #serve para achar quantas vezes se repete o caractere
print(frase.find('ira')) #indica onde começa a sequencia de caracteres indicada
print('Nicolas' in frase) #ele diz se existe ou n essa palavra na frase
print(frase.replace('Nicolas','CR7')) #substitui uma palavra
print(frase.upper()) #tudo maiusculo
print(frase.lower()) #tudo minusculo
print(frase.capitalize()) #primeira letra da frase maiuscula
print(frase.title()) #primeira letra de cada palavra maiuscula
#frase.strip() tira os espaços inuteis e coloca antes do strip r ou l para escolher so um lado para remover
print('-'.join(frase.split())) #separa e junta com o '-'