#List compression=A concise way to create lists in py, compact and easier compared to traditional list

squares=[]

for counter in range(0,10):
    squares.append(counter*counter)
    
print(squares)

#There is a simple way to write the programme above 


#[expression for value in iterable if condition]


squares_part2=[num * num for num in range(0,11)]

print(squares_part2)

tripples=[num * 3 for num in range(0,11)]

print(tripples)

#Making a list of fruits uppercase using list compression


fruits=["apples","bananas","mangoes","coconut","cheese"]

fruits=[ fruit.upper() for fruit in fruits]

print(fruits)

#A sample programme that returns all the positive numbers in a list, using list compression
 
set_numbers=[1,2,3,-4,-5,-6,-7,-8,9,10]

positive_numbers=[ num for num in set_numbers if num>=0]

print(positive_numbers)

#lets harvest all the negative numbers 


negative_numbers=[ num for num in set_numbers if num<0]

print(negative_numbers)

#now a coding exercise with a bunch of exercises 

list_numbers = [3, 8, 12, 5, 7, 18, 21, 2, 10]

#Tasks

#Create a new list containing only the even numbers.

even_numbers=[num for num in list_numbers if num % 2 == 0]

print(even_numbers)

#A square of all the numbers

square_numbers=[ num * num for num in list_numbers]

print(square_numbers)

#create a list of  numbers greater than 10 but add one to each num

greater_than_ten=[num+1 for num in list_numbers if num>10]

print(greater_than_ten)

#create for the numbers

string_numbers=[f"number:{num}"for num in list_numbers]

print(string_numbers)