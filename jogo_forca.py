erros = []
acertos = []
palavra = 'jonathan'

#Função para mostrar se a letra existe na palavra. Exibe quais letras já foram chutadas (separadas por certas e erradas)

def forca(tent):
    if tent in palavra:
        acertos.append(tent)
        print("A letra", tent, "existe")
        print('Letras acertadas: ', acertos)
        print('Letras erradas ', erros)
        print("")

    else:
        erros.append(tent)
        print("A letra", tent, "não existe na plavra")
        print('Letras acertadas: ', acertos)
        print('Letras erradas ', erros)
        print("")

#função para reiniciar o jogo. Possui tambem alternativa de poder chutar a palavra toda e exibir a quantidade de tentativas restantes

def game():
    jogadas = 10
    contador = 0
    while contador < 2:
        print("É Um nome masculino com 8 letras")
        tentativa = input("Insira uma letra pra ver se ela existe na palavra: ")
        forca(tentativa)
        jogadas -= 1
        print(f"Você possui mais {jogadas} jogada(s)")
        print("")
        continuar = input("Deseja chutar o nome?(S) ou (N): ")
        if continuar == 's':
            chute = input("Escreva o nome: ")
            if chute == palavra:
                print("")
                print("PARABÉNS, VOCÊ ACERTOU!")
                break
            else:
                print("")
                print("Que pena, você errou :(")
                break
        contador += 1


game()

print("")
print("-" * 30)
print(f"A palavra certa é: {palavra}")
print("-" * 30)
print("")


def reiniciar():
    novamente = input("Deseja jogar novamente? (S) ou (N) ")
    if novamente == 's':
        game()
    elif novamente == 'n':
        exit()
    else:
        print("")
        print("Insira (s) para SIM ou (n) para NÃO: ")
        print('')
        reiniciar()


reiniciar()
