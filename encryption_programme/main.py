import random

import string

chars=string.digits + string.punctuation + string.ascii_letters + " "

chars_list=list(chars)

plain_text=input("Enter the message that you would like to encrypt: ")

cipher_text=""

key=chars_list.copy()

random.shuffle(key)

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
    
print(plain_text)

print(cipher_text)
    
    