import random

min_value = int(input("Minimum value of number :"))
max_value = int(input("Maximum value of number :"))
no_of_guess = int(input("Number of Guesses ? "))

number_to_guess = random.randint(min_value,max_value)

for n in range(1,no_of_guess + 1,1):
    try:
        guess = int(input("Guess the number: "))

        if guess < number_to_guess:
            print("Too Low!")
            no_of_guess = no_of_guess - 1
            print("No. of Guess left",no_of_guess)
        elif guess > number_to_guess:
            print("Too High!")
            no_of_guess = no_of_guess - 1
            print("No. of Guess left",no_of_guess)
        else:
            print("Congratulations! The number was ",number_to_guess)
            break
                
    except ValueError:
        print("Please enter a valid Number.")

if guess != number_to_guess:
    print("Number was :",number_to_guess)