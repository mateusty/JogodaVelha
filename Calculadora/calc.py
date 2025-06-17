class Calculador:
    
    def adicao(self, num1, num2):
        print(f'o resultado é {num1 + num2}')

    def subtracao(self, num1, num2):
        print(f'o resultado é {num1 - num2}')

    def multiplicacao(self, num1, num2):
        print(f'o resultado é {num1 * num2}')
    
    def divisao(self, num1, num2):
        try:
            resultado = num1 / num2
            print(f'o resultado é {num1 / num2}')
        except ZeroDivisionError:
            print('Você dividiu um número por zero')