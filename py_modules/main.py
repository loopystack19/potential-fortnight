# module- A file containing code you want to include in your own program, use 'import' to include the module

# we going to import the math module

import math

import example

print(math.pi)

#There is also a shorter way we can write the code above 

import math as m

print(m.pi)

#Sometimes we don't need the whole thing, so we just import something

from math import pi

print(pi)

results=example.pi

print(results)

area=example.calculate_area(10)

print(area)

circumfrence=example.calculate_circumfrence(7)

print(circumfrence)

#if i need a list of all the modules available to me i can just type print(help("module"))

