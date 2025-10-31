#Membership operator->They are used to test whether a value or variable is found in a sequence(string, list, tupel,set or dictionary)

# 1.in->Returns a Boolean value of True or false

#sample programme 


word="APPLE"

letter=input("Guess any letter that might be in the secret word: ")

if letter in word:
    print(f"{letter} was found")
else:
    print(f"{letter} was not found")

#2. not in

word_2="Mangoes"

letter_2=input("Guess a letter that can be found in the secret word: ")

if letter_2 not in word:
    print(f"{letter_2} is not in the secret word")
else:
    print(f"{letter_2} is in the secret word")
    
#lets try a list 

new_list=[1,2,3,4,5]

number=int(input("Guess a number that can be found in our secret list: "))

if number not in new_list:
    print(f"{number} is not in the list")
else:
    print(f"{number} is in the list")
    
#Lets try sets

fruits={"Apple","Banana","Coconut","Egg plant","pineapple"}

fruit=input("Guess one fruit that can be found in our set: ")

if fruit not in fruits:
    print(f"{fruit} is not in the set")
else:
    print(f"{fruit} is in the set")
    
#lets try dictionaries

my_dictionary={1:"Apple",
               2:"Banana",
               3:"Carrot",
               4:"cucumber"}

for key, value in my_dictionary.items():
    print(f"{key}={value}")
    


