#The luhn algorithim

#Dummy card=1234 5678 0987 1234

print("A sample programme to check the validity of a credit card")

print()

print("---------------------------------------------------------")

print()

credit_card_number=input("Enter credit card number: ")

while len(credit_card_number)<16:
    credit_card_number=input("please enter a valid credit card number: ")
    
if " " in credit_card_number:
   credit_card_number=credit_card_number.replace(" ","")
       
elif "-" in credit_card_number:
    credit_card_number=credit_card_number.replace("-","")
    
number_list=[]

for number in credit_card_number:
    number_list.append(number)
    
odd_sum=0

doubled_sum=0


for counter in range(len(number_list)-1,-1,-2):
    odd_sum+=int(number_list[counter])
    
    
for counter in range(len(number_list)-2,-1,-2):
    doubled=int(number_list[counter]) * 2
    if double > 9:
        double-=9
    doubled_sum+=doubled
        
        
total_sum=odd_sum + doubled_sum


if total_sum % 10 == 0:
    print(f"{credit_card_number} This is a valid credit card number")
else:
    print(f"{credit_card_number} This is an invalid credit card number")



