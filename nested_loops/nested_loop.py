# a sample programme that prints a rectangle, based on the number of coulmns and rows a user wants

rows_num=int(input("How many rows would you like in your rectangle: "))

column_nums=int(input("How many clomns would you like in your rectangle: "))

symbol_displayed=input("Choose any symbol to be displayed: ")

for counter1 in range(0, rows_num+1):
    for counter2 in range(0, column_nums+1):
        print(symbol_displayed, end="")
    print()