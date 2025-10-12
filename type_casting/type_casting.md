**Type casting**

-Type casting is the process of converting a variable from one data type to another, it involves the use of the following functions str(), int(), bool(), float()

**sometimes in a programme we may need to evaluate the type of data we have, so we use the type() to find in which catergory does a variable belong especially when handling user input**


**sample programme**


full_name="Jafar Maalim Hussein"

print(type(full_name))

**type casting sample programmes**

1.Type casting an integer to a float

age=25

age=float(age)

print(type(age), age)

2.Type casting a float to an integer

distance=12.5

distance=int(distance)

print(type(distance), distance)

3.Type casting an integer into a string

distance=12

distance=str(distance)

print(type(distance), distance)

4.Type casting a boolean into a string

is_student=True

is_student=str(is_student)

print(type(is_student), is_student)