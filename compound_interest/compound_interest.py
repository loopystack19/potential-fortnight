#A simple python calculator that either calculates simple interest or compound interest based on the user inputs 

import math 

user_choice=int(input("Choose 1 for the simple interest calculator, 2 for the compound interest calculator: "))

while not user_choice == 1 and not user_choice == 2:
    print("You can only input either 1 or 2 ")
    user_choice=int(input("Choose 1 for the simple interest calculator, 2 for the compound interest calculator: "))
    
if user_choice == 1 :
    principal=int(input("Input the principal amount you choose to save: "))
    rate=int(input("Input the rate that your local bank offered: (this should be in the percentage format e.g. 20%)"))
    time=int(input("How long do you intend to invest: "))
    simple_interest= principal + (principal * (rate/100) * time)
    print(f"The final amount in your account will be {simple_interest:.3f}")
else:
    principal=int(input("Input the principal amount you choose to save: "))
    rate=int(input("Input the rate that your local bank offered: (this should be in the percentage format e.g. 20%)"))
    time=int(input("How long do you intend to invest: "))
    compound_interest= principal * ((1 + (rate / 100))**time)
    print(f"The final amount is {compound_interest:.3f}")