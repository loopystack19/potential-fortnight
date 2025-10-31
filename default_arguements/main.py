#default arguements-A value for certain parameters default is used when that argument is omitted, this makes your function more flexible and reduce the number of arguements 
import time

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1-tax)

print(net_price(500))

#Basically in simple terms default arguements take place when no other arguements are provided when the function is called 

def count(start, end):
    for counter in range(start, end+1):
        print(counter)
        time.sleep(1)
    print("DONE")
    
count(0,20)


#Note that when you have a default arguements in your function they come after the positional arguements

def default_count(end, start=0):
    for counter in range(start,end+1):
        print(counter)
        time.sleep(1)
    print("WE DONE")
    
default_count(30,5)

