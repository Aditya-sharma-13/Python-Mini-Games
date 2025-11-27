import random

while True:
    Choice = input("Roll the Dice (Y/N): ").lower()
    if Choice == "y":
        
        Dices = int(input("How many Dice do u want to roll ? : "))

        for n in range(1,Dices + 1,1):
            die =random.randint(1,6)
            print(f'({die})')
        
    elif Choice == "n":
        print("Thank You for Playing :)")
        break

    else:
        print("Invalid Choice !")

