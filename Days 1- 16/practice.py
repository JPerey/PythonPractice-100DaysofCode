import random

cont = input("do you want to flip - yes or no: ")

while(cont == "yes"):
    rand_choice = random.randint(0,1)
    if(rand_choice == 0):
        print("heads")
    else:
        print("tails")
    cont = input("do you want to flip - yes or no: ")

