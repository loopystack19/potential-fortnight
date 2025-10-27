**sets**-A collection of unique elements , no dublicates

**creation of a set**- fruits={}

my_fruits={"apples", "bananas","mangoes"}

**to create an empty set you need the set constructor**

my_empty_set=set()

**Adding an element to a set**

my_set={1,2,3,4}

my_set.add(5)

print(my_set)

**output**->{1, 2, 3, 4, 5}

**removing an element in a set**

my_set={1,2,3,4}

my_set.remove(4)

print(my_set)

**note- When using .remove an the element is not present in the list this raises an error, so the better option to use is .discard()**

**output**->{1,2,3}

my_set.pop()->removes an element from the set

**sample programme**

#Given a set of elements remove a random element and print both the element and the updated element

numbers = {10, 20, 30, 40, 50}

print(numbers.pop())

print(numbers)

my_set.clear()->removes all the elements from the set

**my_set{}- is immutable meaning that once its initialized the values cannot be changed, inability to modify in place


**given two sets, find the common element**

-Note an intersection in python, returns common elements from a collection

**sample programme**

#Given a set with a couples of elements, can you use intersection to locate, the common element in both sets

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C=A & B

print(C)


#Given a set with a couples of elements, can you use intersection to locate, the common element in both sets

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C=A.intersection(B)

print(C)

**output**->{3,4}

#given two sets return a set that includes elements that are only unique to one set

A = {"apple", "banana", "mango"}
B = {"banana", "grape", "orange"}

C=set()


for fruit in A:
    if  not fruit in B:
        C.add(fruit)
        
for fruit1 in B:
    if not fruit1 in A:
        C.add(fruit1)
        
print(C)
        
**A shorter way of doing this**

#given two sets return a set that includes elements that are only unique to one set

A = {"apple", "banana", "mango"}
B = {"banana", "grape", "orange"}

C= A ^ B

print(C)
        

Or

#given two sets return a set that includes elements that are only unique to one set

A = {"apple", "banana", "mango"}
B = {"banana", "grape", "orange"}

C= A.symmetric_difference(B)

print(C)
        

**Subset in py**

-A is a subset of B if every element in A is in B

-A is a superset of B if B is a subset of A

#given two sets find if one is either the subset or the superset of the other 

students_A = {"Ali", "Brian", "Cathy", "Diana"}
students_B = {"Cathy", "Diana", "Eli", "Faith"}

if students_A.issubset(students_B):
    print("students_A are a subset of students_B")
else:
    print("students_B are a superset of students_A")

