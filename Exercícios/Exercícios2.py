# letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# numero_antes = int(input('Número da letra do alfabeto: '))
# numero_depois = 26 - numero_antes
# while numero_depois > 0:
#     letras_novas = letras.pop(-1)
#     numero_depois -= 1
# else:
#     print(letras)
# Exercício: Escolher um número entre 1 a 26 e retornar um array com o mesmo numero de letras em ordem alfabética

#Implemente uma função que calcule as raízes de uma equação quadrática, caso as raízes sejam complexas (raíz de número negativo), retorne uma mensagem informando isso
# from math import sqrt

# a = float(input('Insira a variável A da equação: '))
# b = float(input('Insira a variável B da equação: '))
# c = float(input('Insira a variável C da equação: '))
# delta = float((b ** 2) - 4 * a * c)
# if delta < 0:
#     print('Essa equação resulta em uma raíz complexa')
#     x1_incompleto = (-b)/(2 * a)
#     x2_incompleto = (-b)/(2 * a)
#     print(f'O resultado da sua equação é: {x1_incompleto}+{sqrt(-delta)}i e {x2_incompleto}+{sqrt(-delta)}i')
# elif (-b - sqrt(delta))/(2 * a) == (-b + sqrt(delta))/(2 * a):
#     print ('Essa equação só tem uma solução', (-b + sqrt(delta))/(2 * a))
# else:
#     print('x1 =', (-b + sqrt(delta))/(2 * a))
#     print('x2 =', (-b - sqrt(delta))/(2 * a))


letras = []
criptografia = []
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def cripto(palavra):
    for i in range(0, len(palavra)):
        letras.append(palavra.upper()[i:i+1])
    for letra in letras:
        criptografia.append(alfabeto.index(letra) + 1)


cripto('mamaco')
print (criptografia)