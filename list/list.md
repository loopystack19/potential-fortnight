**collection**-Collection, a group of elements or variables, in python they can be presented using list, set, tuple

-In other programming languages, list are what we'd call an array

**sample programme**

fruits=["apples","bananas","mangoes","coconut","pineapples"]

print(fruits)

**output**->['apples', 'bananas', 'mangoes', 'coconut', 'pineapples']

**we can access , items at different points of the list using indexing**

-----sample programme----

fruits=["apples","bananas","mangoes","coconut","pineapples"]

print(fruits[0:3])

**Output**->['apples', 'bananas', 'mangoes']


**When can loop through the elements of a list using a loop**

-----sample programme-----

fruits=["apples","bananas","mangoes","coconut","pineapples"]

for counter in range(0, len(fruits)):
    print(fruits[counter])
    counter+=1

**output**->apples
            bananas
            mangoes
            coconut
            pineapples

**We can check if our collection contains a certain item**

----sample programme----

fruits=["apples","bananas","mangoes","coconut","pineapples"]

if "apples" in fruits:
    print("apples are available in your collection")
else:
    print("No apples my friend")

**output**-the if clause is executed

**list allows you to change the elements after the initialization**
fruits=["apples","bananas","mangoes","coconut","pineapples"]

fruits[0]="Dragon fruit"

for fruit in fruits:
    print(fruit)

**output**-> Dragon fruit
bananas
mangoes
coconut
pineapples

list.append("element")->This adds an element at the end of a collection

list.remove("element")->removes the stated element from the list

list.insert(index,"element")->This method inserts an element at a particular index

list.sort()->This sorts all the elements in a list in alphabetical order

list.reverse()->This reverse the order of the elements in the list

list.clear()->This removes all the elements in a list

list.index("element")->This returns the index of the particular element

my_list.sort()->This returns none , because it does the all the sorting in place, while sorted(my_list), does the actual job
