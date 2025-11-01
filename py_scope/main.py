# variable scope= where a variable is visible and accessible 

# scope resolution= (LEGB) local->enclosed->global->built-in


def func1():
    a=1
    print(a)
    
def func2():
    b=2
    print(b)
    
#The above example demonstrate local scope, meaning that if we decided to print b in func1 we would encouter an error, variables declared in a function have local scope meaning that they are not recognized in other functions

#Enclosed scope-This is mostly used in closures, we going to cover this in depth in the furture


#Global scope->This is where a variable is recognised anywhere in the programme

y=10

#sample programme

def func1():
    a=1
    print(a)
    print(y)
    
def func2():
    b=2
    print(b)
    print(y)
    
# y is recognised by both functions

#Built in scope

from math import e

def func1():
    print(e)
    

    



