#match_case_statement-this is a switch in other programming languages


#lets create a simple programme that returns the name of the day of the week that corresponds to a certain number

def check_day(number):
    match number:
        case 1:
            print("SUNDAY")
        case 2:
            print("MONDAY")
        case 3:
            print("TUESDAY")
        case 4:
            print("WEDNESDAY")
        case 5:
            print("THURSDAY")
        case 6:
            print("FRIDAY")
        case 7:
            print("SATURDAY")
        case _:
            print("INVALID INPUT")
            
            
def basic_calculator():
    results=""
    first_number=int(input("Provide the first operand: "))
    
    second_number=int(input("Provide the second operand: "))
    
    operator=input("Provide an operator to be used: (+->Addition, - -> subtraction, *->Multiplication, /->Division, % -> modulus)")
    
    match operator:
        case "+":
            results=first_number + second_number
            print(results)
        case "-":
            results=first_number + second_number
            print(results)
        case "*":
            results=first_number * second_number
            print(results)
        case "%":
            results=first_number % second_number
            print(results)
        case "/":
            results=first_number / second_number
            print(results)
        case _ :
            print("INTERNAL ERROR")
            


basic_calculator()
            