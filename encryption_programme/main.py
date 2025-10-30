# A simple encryption programme in python

import random

import string

chars="" + string.punctuation + string.digits + string.ascii_letters  

chars=list(chars)

key=chars.copy()

random.shuffle(key)

#This is where the encryption will be taking place 

plain_text=input("Enter the message that you would like encrypted: ")

cipher_text=""


for letter in plain_text:
    if letter in chars:
        index=chars.index(letter)
        cipher_text+=key[index]
    
print(f"This is the plain_text {plain_text}")

print(f"This is the encrypted message: {cipher_text}")