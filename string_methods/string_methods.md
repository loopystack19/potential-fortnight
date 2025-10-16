**String Methods**

-String methods help us to sometimes validate user input or manipulate strings based on our needs 

-Here are some useful string methods

1.len()-Returns the length of a particular string

**sample len() programme**

name="Jafar Hussein"

print(len(name))

output-13

2.find("Character")-returns the index of the first occurence of a particular character, works like a mini search engine

**sample find() programme**

name="Jafar Hussein"

result=name.find("u")

print(result)

output-7, note it also counts the spaces

3. .rfind()-This returns the index for the last occurence of a particular character

name="Jafar Hussein"

result=name.rfind("a")

print(result)

output-3


4. .capitalize()-returns a new string that has been capitalized, note that if the is a space seperating two strings it only capitalizes the first character of the first string

name="jafarhussein"

result=name.capitalize()

print(result)

output-Jafarhussein

5. upper()-capitalizes all the characters of a string

sample programme

name="jafarhussein"

result=name.upper()

print(result)

output-JAFARHUSSEIN

6. .lower()-changes all the characters in a string to lower case 

name="jafarhussein"

result=name.upper()

print(result)

output-jafarhussein

7. isDigit()-Returns a boolean value of true if all the characters in a string are numbers  else false


name="jafarhussein"

result=name.isDigit()

print(result)

output-false 

8. isalpha()-returns true if a string contains only alphabetical characters 


9. .count("characater")-returns an integer that shows the number of occurence for a particular character


name="jafarhussein"

result=name.count("a)

print(result)

output-2

10. .replace("character_being_replaced", "character_being_introduced")-replaces all the occurences of a character with a new character

11. .help(str)-this shows you all the available string methods available to you in python


**sample programme combining everything i just learned**

#Validate user input exercise

#Ensure userName is no more than 12 characters

#ensure user name does not contain any spaces 

#ensure username does not contain any numbers


userName=input("What is user name ?: ")

if len(userName) > 12:
    print("Your user name cannot have more than 12 characters")
elif  not userName.find(" ") == -1:
    print("Your user name cannot contain any spaces")
elif  not userName.isalpha() == True:
    print("Your user name should only contain alphabetical characters")
else:
    print(f"Welcome {userName}")


