
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



