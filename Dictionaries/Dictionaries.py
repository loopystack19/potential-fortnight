#Dictionaries are composed of key value pairs, they are ordered and changeable, No duplicates allowed

capitals={"Kenya":"Nairobi","USA":"washington D.C","China":"Beijing"}

#Dictionaries have a few useful methods and functions

#Dictionary.get("Key")-?>This returns the particular value associated with a particular key, if the key is none existent, the method returns none

city1=capitals.get("Kenya")

print(city1)

#The output here is Nairobi

#Dictionary.update({"key":"value"})->This method allows you to add, or update an existing key value pairs

capitals.update({"Kenya":"Mombasa"}) #-This updates the capital of kenya from nairobi to Mombasa

#Dictionary.pop("key")->This method removes the key and the value associated with it

capitals.popitem()

print(capitals)

#Dictionary.popitem()->This removes the last key value pair in the dictionary

#Dictionary.keys()->Returns a list of all the available keys in a dictionary

#Dictionary.values()->Returns a list of all the values in a dictionary

#Dictionary.items()->Returns a 2d tupel of lists, each list is made up of the key value pairs

#individual_capitals=capitals.items()

#print(individual_capitals)

#output->dict_items([('Kenya', 'Mombasa'), ('USA', 'washington D.C')])

#sample programme of that 


for key, value in capitals.items():
    print(f"{key}: {value}")





