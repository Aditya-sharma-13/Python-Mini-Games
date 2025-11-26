import random

choices = ('r','p','s')
emoji = {'r':'🪨','p':'📜','s':'✂️'}

while True:
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emoji[user_choice]}')
    print(f'Computer chose {emoji[computer_choice]}')

    if user_choice == computer_choice:
        print("Tie!")

    elif(
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        print("You win!")

    else:
        print("You Lose")

    resume = input("Continue? (y/n): ").lower()
    if resume == 'n' :
        break
