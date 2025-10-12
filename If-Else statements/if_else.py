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