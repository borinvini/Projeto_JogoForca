import jogo as j

def mostrar_menu():
    print("="*30)
    print(" " * 7 + "JOGO DA FORCA")
    print("="*30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR\n")
    print("="*30)


while True:
    mostrar_menu()
    
    opcao = int(input('Escolha uma opção (1/2/3): '))
    
    if opcao == 1:
        print('Iniciar jogo!')
        j.jogar()
        input('Digite qualquer tecla para continuar...')
    
    elif opcao == 2:
        print('Mostrar score!')
        
    elif opcao == 3:
        print('Saindo do jogo. Até mais!')
        break
    
    else:
        print('Opção inválida! Tente novamente!')