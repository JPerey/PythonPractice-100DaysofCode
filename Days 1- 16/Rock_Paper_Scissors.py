# --Imports--
import random

# --Imports--

print("Would you want to play Rock, Paper, Scissors (RPS)?")
rps_choice = input("y or n: ")

while( rps_choice == "y"):

    print("What do you choose: 0 - Rock, 1 - Paper, 2 - Scissors")
    player_rps = int(input("0, 1, or 2: "))
    
    pc_rps = random.randint(0,2)
    print(f"pc picked {pc_rps}")

    if (player_rps == 0 and pc_rps == 0):
        print("TIE")
    elif (player_rps == 0 and pc_rps == 1):
        print("pc won!")
    elif (player_rps == 0 and pc_rps == 2):
        print("player won!")

    elif (player_rps == 1 and pc_rps == 0):
        print("player won!")
    elif (player_rps == 1 and pc_rps == 1):
        print("TIE")
    elif (player_rps == 1 and pc_rps == 2):
        print("pc won!")

    elif (player_rps == 2 and pc_rps == 0):
        print("pc won!")
    elif (player_rps == 2 and pc_rps == 1):
        print("player won!")
    elif (player_rps == 2 and pc_rps == 2):
        print("TIE")


    print("Another round of play Rock, Paper, Scissors (RPS)?")
    rps_choice = input("y or n: ")

print("Game Over!")