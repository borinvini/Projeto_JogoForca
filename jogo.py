import desenhos as d
from random import choice 

def jogar():
    lista_palavras = list()
    arquivo = open('palavras.txt', 'r')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)
        
    palavra_sorteada = choice(lista_palavras)

    for x in range(50):
        print()
        
    digitadas = []
    acertos   = []
    erros     = 0

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
        
        # * CONDIÇÃO DE VITÓRIA
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break
        
        # * TENTATIVAS
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou essa letra!')
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')
                
        
        d.desenhar_forca(erros)
        
        # * CONDIÇÃO DE FIM DE JOGO
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correta era {palavra_sorteada}.')
            break
