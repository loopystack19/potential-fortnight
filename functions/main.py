# functions in python kinda look weird hahahaha 

#I don't think i need to define a function but here goes nothing, insted of writing a bunch of line for the same stuff, imagine if you could call one line of code that does all that stuff

#The return key word in functions-in some situations a function is needed to return an output, imagine adding two  numbers you'd need to return the results 

#sample function that receives a word and returns the reversed version of it

def reverse_sentence(sentence):
    reversed_sentence=""
    for counter in range(len(sentence)-1,-1,-1):
        reversed_sentence+=sentence[counter]
    return reversed_sentence

print(reverse_sentence("hello"))

#A sample programme to calculate the area of a rectangle 

def calculate_area():
    length=int(input("Enter the length of your rectangle: "))
    while length<=0:
       length=int(input("Enter the length of your rectangle: "))    
    width=int(input("Enter the width of your rectangle: "))
    while width<=0:
        width=int(input("Enter the width of your rectangle: "))  
    area=length*width
    print(f"The area of your rectangle is {area}")
    return area

calculate_area()

# A function that takes three numbers and returns the largest of the three

def find_max_num():
    first_num=float(input("Enter the first number: "))
    second_num=float(input("Enter the second Number: "))
    third_num=float(input("Enter a third number: "))
    maximum_num=max(first_num, second_num, third_num)
    return f"The largest number of the three is {maximum_num}"

print(find_max_num())


# A function that checks if a number is either even or odd

def check_num():
    num=int(input("Enter a number you would like to check: "))
    if num<0:
        num=int(input("Enter a number that is greater than zero: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        
    
check_num()
    

    
#Note that functions are able to accept actual arguements when parameters are included during the initialization process

