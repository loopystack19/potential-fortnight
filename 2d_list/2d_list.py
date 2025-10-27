
fruits=["apples","bananas","mangoes","pineapples"]

vegies=["cucumber","celery","brocolli","onions"]

meat=["fish","chicken","turkey", "beef"]

groceries=[fruits, vegies, meat]

for row in range(0, len(groceries)):
    for column in range( 0, len(groceries)):
        print(groceries[row][column], end="        ")
    print()
    
#2d list are like 2 dimension arrays in other languages , beasically its made of individual list

#sample programme creating a 2d keypad that we see on phones

list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
list4=["*",0,"#"]

phone=[list1,list2,list3,list4]


for row in phone:
    for element in row:
        print(element ,end="")
    print()