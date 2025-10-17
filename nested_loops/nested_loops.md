**Nested loops**

-Honestly i feel like i have really struggled with nested loops in other languages, but i think now i have full grasp of what nested loops are and how they work

**sample programme**

rows_num=int(input("How many rows would you like in your rectangle: "))

column_nums=int(input("How many clomns would you like in your rectangle: "))

symbol_displayed=input("Choose any symbol to be displayed: ")

for counter1 in range(0, rows_num+1):
    for counter2 in range(0, column_nums+1):
        print(symbol_displayed, end="")
    print()