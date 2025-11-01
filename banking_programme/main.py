# A simple banking programme

def show_balance():
    print(f"Your bank balance is ${balance:.2f}")

def deposit():
    amount=float(input("Enter an amount that you would like to deposit: "))
    
    if amount<0:
        print("Thats an invalid input")
        return 0
    else:
        return amount

def withdraw():
    amount=float(input("Enter an amount to be withdrawn: "))
    
    if amount>balance:
        print("INSUFFICIENT FUNDS IN YOUR ACCOUNT")
        return 0
    elif amount<0:
        print("Amount should be greater than zero")
        return 0
    else:
        return amount

balance=0

is_running=True

print("-------Welcome-------")

print()


print("-----A SIMPLE BANKING PROGRAMME--------")

print()


while is_running:
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    choice=input("Enter a choice (1-4): ")
    
    if choice == "1":
        show_balance()
    elif choice =="2":
        balance+=deposit()
    elif choice == "3":
        balance-=withdraw()
    elif choice == "4":
        is_running=False
    else:
        print("Thats an invalid response")
        
print("Thank you for banking with us")
    