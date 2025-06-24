from tkinter import *

root = Tk()
root.title('Jogo da Velha')

#Lista de números entre 1 a 9, arranjados em um grid 3x3 para se assemelhar aos botões, cada botão está associado a um número
#a soma das linhas e diagonais sempre será 15, e é a única forma para ter tal resultado.
board = [[2, 7, 6],
         [9, 5, 1],
         [4, 3, 8]]

#Lista de números relacionados aos quadrados de cada jogador
x = []
o = []

#Função que define o ganhador, caso a soma de 3 números nas listas x ou o, seja = 15
def Ganhador(nums):
    nums.sort()  
    for i in range(len(nums) - 2):
        esquerda, direita = i + 1, len(nums) - 1
        while esquerda < direita:
            soma = nums[i] + nums[esquerda] + nums[direita]
            if soma == 15:
                return True
            elif soma < 15:
                esquerda += 1
            else:
                direita -= 1
    return False

#Função que muda os botões quando cada jogador os aperta, também adiciona nas listas x e o um número entre 1 a 9 para definir o vencedor
#utilizando a função acima
def Escolha(num):
    Escolha.counter += 1
    if Escolha.counter % 2 == 0:
        exec(f'botao{num}.config(text="X", state=DISABLED)')
        if num <= 3:
            x.append(board[0][num - 1])
        elif num >= 3 and num <= 6:
            x.append(board[1][num-4])
        else:
            x.append(board[2][num-7])
        if Ganhador(x) == True:
            ganhador.config(text='"X" GANHOU!!!!!!')
    else:
        exec(f'botao{num}.config(text="O", state=DISABLED)')
        if num <= 3:
            o.append(board[0][num - 1])
        elif num >= 3 and num <= 6:
            o.append(board[1][num-4])
        else:
            o.append(board[2][num-7])
        if Ganhador(o) == True:
            ganhador.config(text='"O" GANHOU!!!!!!')

#Define de quem é a vez
Escolha.counter = 0

#Função que limpa todos os botões
def Clear():
    for i in range(1, 10):
        exec(f'botao{i}.config(text="", state=NORMAL)')
        x.clear()
        o.clear()
    ganhador.config(text='Sem Ganhador')

#Criando os botões e colocando eles em ordem 3x3

botao1 = Button(root, padx=25, pady= 20, command= lambda: Escolha(1))
botao1.grid(column=1 ,row=2)
botao2 = Button(root,  padx=25, pady= 20, command= lambda: Escolha(2))
botao2.grid(column=2 ,row=2)
botao3 = Button(root,  padx=25, pady= 20, command= lambda: Escolha(3))
botao3.grid(column=3 ,row=2)
botao4 = Button(root, padx=25, pady= 20, command= lambda: Escolha(4))
botao4.grid(column=1 ,row=3)
botao5 = Button(root, padx=25, pady= 20, command= lambda: Escolha(5))
botao5.grid(column=2 ,row=3)
botao6 = Button(root, padx=25, pady= 20, command= lambda: Escolha(6))
botao6.grid(column=3 ,row=3)
botao7 = Button(root, padx=25, pady= 20, command= lambda: Escolha(7))
botao7.grid(column=1 ,row=4)
botao8 = Button(root, padx=25, pady= 20, command= lambda: Escolha(8))
botao8.grid(column=2 ,row=4)
botao9 = Button(root, padx=25, pady= 20, command= lambda: Escolha(9))
botao9.grid(column=3 ,row=4)
ganhador = Label(root, text='Sem Ganhador')
ganhador.grid(column=3, row=5, columnspan=1)

clear = Button(root, text='CLEAR', padx= 45, pady= 20, command= Clear)
clear.grid(column=1, row=5, columnspan=2)


root.mainloop()

#Fazer um jogo da velha sem o tkinter, somente no terminal