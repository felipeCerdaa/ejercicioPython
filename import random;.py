import random;

'''
    Tijera corta a papel, 
    papel tapa a piedra, 
    piedra aplasta a lagarto, 
    lagarto envenena a Spock, 
    Spock rompe a tijera, 
    tijera decapita a lagarto, 
    lagarto devora a papel, 
    papel desautoriza a Spock, 
    Spock vaporiza a piedra, y como siempre, 
    piedra aplasta a tijera
'''


def select():
    print("tijera, papel, piedra, lagarto, Spock")
    player1 = input("ingrese su eleccion: ")
    player1 = player1.lower()
    return player1

def player_compute():
    player_compute = random.choice(["tijera", "papel", "piedra", "lagarto", "Spock"])
    return player_compute

def game(player1, player_compute):
    if(player1 == player_compute):
        print("empate")
    elif(player1 == "tijera" and player_compute == "papel" or player1 == "tijera" and player_compute == "lagarto"):
        print("gana player1 => ", player1 , " => ", player_compute)
    elif(player1 == "papel" and player_compute == "piedra" or player1 == "papel" and player_compute == "Spock"):
        print("gana player1 => ", player1 , " => ", player_compute)
    elif(player1 == "piedra" and player_compute == "lagarto" or player1 == "piedra" and player_compute == "tijera"):
        print("gana player1 => ", player1 , " => ", player_compute)
    elif(player1 == "lagarto" and player_compute == "spock" or player1 == "lagarto" and player_compute == "papel"):
        print("gana player1 => ", player1 , " => ", player_compute)
    elif(player1 == "spock" and player_compute == "tijera" or player1 == "spock" and player_compute == "piedra"):
        print("gana player1 => ", player1 , " => ", player_compute)
    else:
        print("ganaste hijo mio", player_compute, " => ", player1)



""" select()
player_compute() """
game(select(), player_compute())