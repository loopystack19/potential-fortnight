#Validate user input exercise

#Ensure userName is no more than 12 characters

#ensure user name does not contain any spaces 

#ensure username does not contain any numbers


userName=input("What is user name ?: ")

if len(userName) > 12:
    print("Your user name cannot have more than 12 characters")
elif  not userName.find(" ") == -1:
    print("Your user name cannot contain any spaces")
elif  not userName.isalpha() == True:
    print("Your user name should only contain alphabetical characters")
else:
    print(f"Welcome {userName}")