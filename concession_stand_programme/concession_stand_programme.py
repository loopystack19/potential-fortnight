#so first we create a menu of all the items and their prices

menu={"pizza":3.00,
      "nachos":4.50,
      "soda":3.25,
      "fries":1.75,
      "chips":2.50,
      "kfc":25.60
      }

cart=[]

total=0


# we going to print all the items in our menu and prompt the user to choose what they would like

print("--------MENU---------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
    
print("-----------------------")


while True:
    food=input("Choose the foods on the menu that you would like to order:(q to quit)   ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
        
for food in cart:
    total+=menu.get(food)
    

print("------YOUR ORDER-------")

for food in cart:
    print(food, end=" ")
    
print()

print(f"Your total is ${total:.2f}")


print("------------------------")