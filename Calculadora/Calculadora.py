from calc import Calculador
continuar = True
objeto = Calculador()
escolha = 1
while continuar == True:
    a = float(input('Insira um primeiro número: '))
    b = float(input('Insira um segundo número '))

    continuar = False

    while escolha != 0:
        print('')
        print('0 - Fechar')
        print('1 - Soma')
        print('2 - Subtrair')
        print('3 - Multiplicar')
        print('4 - Dividir')
        print('5 - Mudar números')
        print('')
        escolha = int(input(''))
        if escolha == 1:
            objeto.adicao(a, b)
        elif escolha == 2:
            objeto.subtracao(a, b)
        elif escolha == 3:
            objeto.multiplicacao(a, b)
        elif escolha == 4:
            objeto.divisao(a, b)
        elif escolha == 5:
            continuar = True
            break
        elif escolha == 0:
            break
        else:
            print('Escolha inválida!')
            