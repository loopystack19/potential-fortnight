#An intermediate question on control structures

import math

math_score=int(input("What did you score in the maths test bro?: "))

science_score=int(input("What did you score in the science test bro?: "))

english_score=int(input("What did you score in your english test?: "))

average_score=math.floor((math_score + science_score + english_score)/3)

if(average_score >=90 and (math_score>=80 and science_score>=80 and english_score>=80) ):
    grade="A"
    print(grade)
elif(average_score>=80 and ((math_score >=75 and science_score>=75 and english_score<=75) or (math_score >=75 and science_score<=75 and english_score>=75) or (math_score <=75 and science_score>=75 and english_score>=75))):
    grade="A"
    print(grade)
elif(average_score>=70 and (((math_score>=60 and science_score>=60 and english_score>=60)))):
    grade="B"
    print(grade)
elif(average_score>=60 and ((math_score<=50 or science_score<=50 or english_score<=50))):
    grade="C"
    print(grade)
elif(math_score<=40 or science_score<=40 or english_score<=40):
    grade="FAIL"
    print(grade)
else:
    grade="D"
    print(grade)


