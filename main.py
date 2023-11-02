palavra = input('Digite uma palavra secreta: ').lower().strip()

for x in range(50):
    print()
    
digitadas = []
acertos   = []
erros     = 0

while True:
    # * IMPRIME NA TELA A PALAVRA SECRETA
    adivinha = ""
    for letra in palavra:
        if letra in acertos:
            adivinha += letra
        else:
            adivinha += '\u2588'
    print(f'ADIVINHE ({len(palavra)} letras): ')
    for letra in adivinha:
        print(f'{letra} ', end='')
    print()
    
    # * CONDIÇÃO DE VITÓRIA
    if adivinha == palavra:
        print('Você acertou!')
        break
    
    # * TENTATIVAS
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já usou essa letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
            
    
    # * DESENHANDO A FORCA        
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print('X  O  ')
    else:
        print('X')
        
    linha2 = ""
    if erros == 2:
        linha2 = "  | "
    elif erros == 3:
        linha2 = " /| "
    elif erros >= 4:
        linha2 = " /|\ "
    print(f"X{linha2}")
    
    linha3 = ""
    if erros == 5:
        linha3 += " / "
    elif erros >= 6:
        linha3 += " / \ "
    print(f"X{linha3}")
    
    print(f"X\n=======")
    
    # * CONDIÇÃO DE FIM DE JOGO
    if erros == 6:
        print('Enforcado!')
        print(f'A palavra correta era {palavra}.')
        break
