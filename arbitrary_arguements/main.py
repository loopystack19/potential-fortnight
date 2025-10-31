
# *args=allows you to pass multiple non-key arguments

# **kwargs=allows you to pass multiple keyword-arguments

# *-this is the unpacking operator

#sample programme 1

def add(a,b):
    return a + b

print(add(1,2))

#In the function above we can only provide two positional arguements , but using the *args we can provide an infinite number of arguements, note that all the arguements are packed in a tupel


def modified_add(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(modified_add(1,2,3,4))


#Now we going to do something to deal with **kwargs


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="Bikini Bottom",city="Nairobi",country="Kenya",continent="Africa")


# A sample programme that combines both 


def shipping_address(*args,**kwargs):
    for arg in args:
        print(arg, end="")
    print()
    
    for key, value in kwargs.items():
        print(f"{key}:{value}")


shipping_address("MR.","Jafar","Hussein",
                 street="123 fake",
                 city="Bikini Bottom",
                 house="Pineapple house")





 