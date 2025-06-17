#Exercício 1

# login = input('Insira o usuário: ')
# tentativas_login = 0
# tentativas_max = 3
# falha_login = False
# falha_senha = False
#
# while login != 'admin':
#     login = input(f'Você tem mais {tentativas_max - tentativas_login}, Insira o login novamente: ')
#     if tentativas_login != tentativas_max:
#         tentativas_login += 1
#     else:
#         falha_login = True
#         break
#
# senha = input('Insira a senha: ')
#
# while senha != 'senha123':
#     if falha_login == True:
#         break
#     else:
#         senha = input(f'Você tem mais {tentativas_max - tentativas_login}, Insira a senha novamente: ')
#         if tentativas_login != tentativas_max:
#             tentativas_login += 1
#         else:
#             falha_senha = True
#             break
#
# if falha_login or falha_senha == True:
#     print('O login foi bloqueado')
# else:
#     print('Login realizado com sucesso!')

#Exercício 2

# soma = 0
# numero = 1
# while numero > 0:
#     numero = int(input('Digite um numero inteiro positivo, caso o numero digitado seja 0, o programa irá somar todos os números anteriores: '))
#     soma = soma + numero
# print(soma)

#Exercício 3

# for i in range(1, 11):
#     print(f'{i} * 1 = {i * 1}     {i} * 2 = {i * 2}     {i} * 3 = {i * 3}      {i} * 4 = {i * 4}       {i} * 5 = {i * 5}')

#Exercício 4
# num = int(input('Digite um numero inteiro positivo: '))
# for i in range(2, num + 1):
#     primo = True
#     for divisor in range(2, i):
#         if i % divisor == 0:
#             primo = False
#             break
#     if primo == True:
#         print(i)

#Exercício 5

# number = int(input('Insira o digito da sequência de Fibonacci:'))
# inicio = [0, 1]
# if number == 1:
#     print (0)
# if number == 2:
#     print(inicio)

# if number >= 3:
#     for i in range(1, number - 1):
#         proximo = inicio[-1] + inicio[-2]
#         inicio.append(proximo)
#     print(inicio)
