import random

while True:
    choices = ["rock", "paper", "scissors"]

    Player = None
    while Player not in choices:
        Player = input("rock, paper, or scissors? ").lower()

    Computer = random.choice(choices)

    if Player == Computer:
        print("Player: ", Player)
        print("Computer: ", Computer)
        print("It's a tie!")
    elif Player == "rock":
        if Computer == "paper":
            print("Player: ", Player)
            print("Computer: ", Computer)
            print("You lose!")
        if Computer == "scissors":
            print("Player: ", Player)
            print("Computer: ", Computer)
            print("You win!")
    elif Player == "paper":
        if Computer == "rock":
            print("Player: ", Player)
            print("Computer: ", Computer)
            print("You win!")
        if Computer == "scissors":
            print("Player: ", Player)
            print("Computer: ", Computer)
            print("You lose!")
    elif Player == "scissors":
        if Computer == "rock":
            print("Player: ", Player)
            print("Computer: ", Computer)
            print("You lose!")
        if Computer == "paper":
            print("Player: ", Player)
            print("Computer: ", Computer)
            print("You win!")

    play_again = input("Do you wanna play again? ").lower()
    if play_again != "yes":
        break

print("See you later!")
