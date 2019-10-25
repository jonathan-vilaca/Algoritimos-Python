print("")
print("Vamos jogar Pedra, Papel e Tesoura?!")
print("              ✊     ✋         ✌")
print("")

#Importando biblioteca GETPASS

import getpass

#Escolher as alternativas:

jogador1 = getpass.getpass("Jogador 1, escolha entre: Pedra, Papel e Tesoura: ").upper().strip()
jogador2 = getpass.getpass("Jogador 2, escolha entre: Pedra, Papel e Tesoura: ").upper().strip()

#Nenhuma alternativa válida:

if (jogador1 not in ("PEDRA", "PAPEL", "TESOURA")) or (jogador2 not in ("PEDRA", "PAPEL", "TESOURA")):
    print(f"Jogador 1 digitou {jogador1} e Jogador 2 digitou {jogador2}. Favor escolher PEDRA, PAPEL ou TESOURA!")

#Possibilidades de alternativas válidadas:

else:
#Possibilidades em que o JOGADOR 1 ganhará:
    if (jogador1 == "PEDRA" and jogador2 == "TESOURA") or (jogador1 == "PAPEL" and jogador2 == "PEDRA") or (jogador1 == "TESOURA" and jogador2 == "PAPEL"):
        print(f"Jogador 1 escolheu {jogador1} e Jogador 2 escolheu {jogador2}. Jogador 1 Venceu!!!")

#Possibilidades em que o JOGADOR 2 ganhará:
    else:
        if (jogador2 == "PEDRA" and jogador1 == "TESOURA") or (jogador2 == "PAPEL" and jogador1 == "PEDRA") or (jogador2 == "TESOURA" and jogador1 == "PAPEL"):
            print(f"Jogador 1 escolheu {jogador1} e Jogador 2 escolheu {jogador2}. Jogador 2 Venceu!!!")

#Possibilidade em que ambos escolheram a mesma alternativa:
        else:
            if jogador1 == jogador2:
                print(f"Empate! Ambos escolheram {jogador1}. Tentem novamente!")