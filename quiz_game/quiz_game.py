questions=("1.Which document guarantees freedom of speech protections in the United States? ",
           "2.Who was the primary author of the Declaration of Independence? ",
           "3.Which U.S. state is known as the “Sunshine State”? ",
           "4.The Supreme Court case Marbury v. Madison established the principle of: ",
           "5. Which river forms part of the natural border between Texas and Mexico?")

options= (("A.The Articles of Confederation",
           "B. The Bill of Rights",
           "C.The Constitution’s Preamble",
           "D.The Emancipation Proclamation"),
         ("A.George Washington","B.Thomas Jefferson","C.James Madison","D.Benjamin Franklin"),
         ("A.California","B.Florida","C. Arizona","D.Hawaii"),
         ("A.Judicial review","B.Freedom of the press","C.Due process","D. Double jeopardy"),
         ("A. Mississippi River","B.Rio Grande","C.Colorado River","D. Brazos River"))

guesses=[]

answers=["B","B","B","A","B"]

question_num=0

score=0


for question in questions:
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Choose A, B, C OR D: ").upper()
    if guess == answers[question_num]:
        print("CORRECT")
        score+=1
    else:
        print(f"INCORRECT, the correct answer is {answers[question_num]}")
    question_num+=1
    

score=(score/len(questions) * 100)


print(f"Your score is {score}")