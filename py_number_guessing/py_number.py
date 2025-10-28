#we going to create a simple number guessing 

import random

lowest_num=1

highest_num=10

answer=random.randint(lowest_num, highest_num)

is_running=True

guesses=0

print("------Py number guessing game 😊 ----------")

print(f"You are going to pick a random number in the range {lowest_num} to {highest_num}")


while is_running:
    guess=input("Enter a guess to see if you'd get the random number: ")
    if guess.isdigit():
       guess=int(guess)
       if guess < answer:
           print("Too low, try again")
           guesses+=1
       elif guess > answer:
           print("Too high, try again")
           guesses+=1
       else:
           is_running=False
           print("CORRECT")
           print()
           print(f"It took you {guesses} guesses")
           print()
           print(f"the answer was {answer}")
    else:
        print("Invalid input")
        print()
        print(f"You are going to pick a random number in the range {lowest_num} to {highest_num}")
        print()
        guess=input("Enter a guess to see if you'd get the random number: ")

