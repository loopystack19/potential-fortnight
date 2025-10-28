#sometimes we may need to generate a random choice, lets for a player playing against an AI , the choices of the ai need to be randomised 

import random

#If you need to generate a random integer here is a sample programme

random_integer=random.randint(1,6)

print(random_integer)

#This generates a random integer in the range of 1 to 6

#if we need a random floating point number, this is what we going to do

floating_point=random.random()

print(floating_point)

#sometimes our programme maybe needed to make a random choice from a set of options

options=["rock","paper","scissors"]

random_choice=random.choice(options)

print(random_choice)

#sometimes in our programme may need to shuffle things around 

card=["2","3","4","5","6","7","8","9","A","K","Q","J"]

random.shuffle(card)

print(card)