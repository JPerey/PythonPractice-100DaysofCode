import sys
choice = 0

# -------------------

print("Welcome to the Jammin treasure island adventure story [with liek 4 choices]")

choice = input("Welcome to Treasure Island. Your mission is to find the treasure.\nLeft or right?: ")

if choice == "left":
    print("Good call.")
else:
    print("Fall into hole.\nGame Over.")
    sys.exit()

choice = input("swim or wait: ")

if choice == "wait":
    print("Good call.")
else:
    print("Attacked by trout.\nGame Over.")
    sys.exit()

choice = input("Which door do you choose - red, blue, or yellow: ")

if choice == "yellow":
    print("You win!")
elif choice == "red":
    print("Burned by fire.\nGame over.")
    sys.exit()
elif choice == "blue":
    print("Eaten by beasts.\nGame over.")
    sys.exit()
else:
    print("Game over.")
    sys.exit()
