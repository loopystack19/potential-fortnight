#A sample programme that allows a user to enter a number, and prints all even Numbers starting from zero to that point 

#While a condition remain true a certain code block continues to execute until the condition is false 

#sample programme - Write a Python program using a while loop to calculate and print the sum of all even numbers between 1 and a user-specified positive integer $N$ (inclusive).

user_input=int(input("Choose a number of your liking?: "))

starting_point=0

total=0

while starting_point <= user_input:
    print(starting_point)
    total+=starting_point
    starting_point+=2
print(f"The total sum of all even numbers upto that point is {total}")
