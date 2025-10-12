**Arithmetics**

-Arithemetics , they help us manipulate data to be specific numbers

**Arithmetic operators**

1.Addition-It's represented with (+)

2.Subtraction_It's represented with(-)

3.Multiplication(*)-It's represented with the asterisk symbol

4.Division(/)-Division is represented with the slash symbol

5.Modulus(%)-The modulus operators is represented by the percentage symbol, it returns the remainder after a division

6.Exponent(**)-The exponenet is represented with double asterisks

7.round()-rounds a number

8.abs()-returns the absolute value of a number

9.max()-returns the maximum number between a set of numbers

10.min()-returns the minimum between a set of numbers 

**To use the following you need to import math before using them**

1.math.pi()-returns all the digits of pi

2.math.e()-returns the digits of exponential constant

3.math.sqrt()-return the square root of a number 

4.math.ceil()-this function rounds up numbers

5.math.floor()-this function rounds number downwards

**sample programme**

**you have a small shop that sells three items: apples, bananas, and oranges. The prices are:

Apples: $0.75 each
Bananas: $0.60 each
Oranges: $0.50 each
You want to create a Python snippet that does the following:

Reads three integers from user input representing the quantities of apples, bananas, and oranges you want to buy.
Computes the total cost using those quantities.
Applies a 8% tax to the total cost.
If the user buys 5 or more items in total, apply a 10% discount on the pre-tax total (before tax); otherwise, no discount.
Prints the final amount you should pay, rounded to 2 decimal places, with a friendly message.**

**solution**


apples_quantity=input("How many apples do you want to buy?: ")

apples_quantity=int(apples_quantity)

bananas_quantity=input("How many bananas do you want to buy?: ")

bananas_quantity=int(bananas_quantity)

oranges_quantity=input("How many oranges do you want to buy?: ")

oranges_quantity=int(oranges_quantity)

apple_price=0.75

banana_price=0.60

orange_price=0.50

tax=0.08

discount=0.01

total_cost=((apples_quantity * apple_price) + (bananas_quantity * banana_price) + (oranges_quantity * orange_price))



total_quantity=apples_quantity + bananas_quantity + oranges_quantity

if total_quantity > 5:
    final_total=round(((total_cost-(total_cost * discount))+(total_cost * tax)),2)

    final_message=(f"Thank you for shopping with us your total after discount and tax is {final_total}")

    print(final_message)
else:
    final_total=round((total_cost+(total_cost * tax)),2)


    final_message=(f"Thank you for shopping with us, your total with tax is {final_total}")

    print(final_message)





