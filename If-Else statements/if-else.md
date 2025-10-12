**If-else statements in python**

if - else statements are used to evaluate a certain condition , if a particular condition is true the if block will execute, if not the esle block will be executed

**sometimes we need to check multiple conditions, so we introduce elif, so if the first condition is true the first block will execute , if false the elif block will execute , if bothe are false, then the else block executes**

**Sample programme**

#A simple age checker that uses if - else statements

age=int(input("How old are you?: "))

if age > 18 and age <=70:
    print("You are considered an adult")
elif age > 0 and age< 18:
    print("You are too young, you still a minor")
else:
    print("You are either too old or you have not been born yet")

**sample programme 2**

#Simple grade checker using  if, elif and else

score=int(input("What was your score in the last maths test?: "))

if score > 90 and score <=100:
    print("You scored an A ")
elif score >=80 and score <=90:
    print("You scored a B")
elif score >=70 and score < 80:
    print("You scored a C")
elif score>=60 and score < 70:
    print("You scored a D")
else:
    print("You failed")

