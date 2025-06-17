#Exercícios 1
def Escrever(nome, texto):
    with open(f'{nome}.txt', 'w') as arquivo:
        arquivo.write(texto)

#Exercícios 2
def Ler(nome):
    with open(f'{nome}.txt', 'r') as leitura:
        return leitura.read(f'{nome}.txt')

Escrever('arquivo', 'Amo Toranjas')
Ler('arquivo')