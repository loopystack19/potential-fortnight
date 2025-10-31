#Iterables=An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop


numbers=[1,2,3,4,5]

for number in  numbers:
    print(number)
    
#Reversing the way stuff are printed

for counter in reversed(numbers):
    print(counter)
    
    
#List are iterable

numbers=[1,2,3,4,5]

for number in  numbers:
    print(number)

#Tupels are iterable

numbers=(1,2,3,4,5)

for number in  numbers:
    print(number)

#sets are iterable

fruits={"apples","Bananas","coconut","Egg plant","Fish"}

for fruit in fruits:
    print(fruit)
    
#Note that sets are not reverseable


#Strings are iterable 

name="spongebobsquarepants"

for letter in name:
    print(letter, end="")
    
#Dictionaries are iterable also

my_dictionary={1:"A",2:"B",3:"C"}

#If you need the key

for key in my_dictionary.key():
    print(key)
    
#If you need values

for values in my_dictionary.values():
    print(values)
    
#If you need both

for key, value in my_dictionary.items():
    print(f"{key}:{value}")
    

