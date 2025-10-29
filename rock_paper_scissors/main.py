# Arandom rock paper scissors game 

import random 

options=("rock","paper","scissors")

player_choice=None

running=True

while running:

    computer_choice=random.choice(options)

    player_choice=input("Choose between rock, paper and scissors: ").lower()

    while player_choice not in options:
         player_choice=input("Choose between rock, paper and scissors: ").lower()
    
    
    print(computer_choice)

    print(player_choice)


    if player_choice == computer_choice:
        print(f"Its a tie: {player_choice} VS {computer_choice}")
    elif player_choice == "rock" and computer_choice == "scissors":
        print(f"Its a Win: {player_choice} VS {computer_choice}")
    elif player_choice == "paper" and computer_choice == "rock":
        print(f"Its a Win: {player_choice} VS {computer_choice}")
    elif player_choice =="scissors" and computer_choice == "paper":
        print(f"Its a win: {player_choice} VS {computer_choice}")
    else:
        print(f"You LOOSE: {player_choice} VS {computer_choice}")
        
    if not input("Would you like to play again(y/n):").lower() == "y":
        running=False
        print("Its a lame game but thanks for playing")
    
    
    
    
    