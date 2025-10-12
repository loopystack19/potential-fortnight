**user input**

-sometimes our programmes need some sort of user input inorder to archieve a certain outcome, there we need to be able to accept, convert and manipulate user input

-input()-This is the function used to prompt a user to enter data and it returns the data in form of a string data type

**sample programme**

#this is a simple calculator to calculate the circumfrence of a circle

radius=input("What is the radius of your circle?: ")

radius=int(radius)

PI=3.1415

circumfrence=(2 * PI * radius)

print(f"The circumfrence of your circle is {circumfrence}")

**The input value allows the user to input the value of the radius of their circle, the programme returns the circumfrence**

