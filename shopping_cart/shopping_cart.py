#A simple simulation of a shopping cart programme

foods=[]

prices=[]

total=0

while True:
    food=input("Enter a food or anything you would like to add in your shopping cart: (press q to exist)")
    foods.append(food)
    if food.lower() == "q":
        break
    else:
        price=float(input("Enter the price for the food choosen: $"))
        prices.append(price)
        
for price in prices:
    total+=price
    
print("-------Here is your shopping cart------")
        
        
for food in foods:
    print(food, end=" ")

print()
    
print(f"Here is your total: ${total:.2f}")
    
    

    
    