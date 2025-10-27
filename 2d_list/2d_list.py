
fruits=["apples","bananas","mangoes","pineapples"]

vegies=["cucumber","celery","brocolli","onions"]

meat=["fish","chicken","turkey", "beef"]

groceries=[fruits, vegies, meat]

for row in range(0, len(groceries)):
    for column in range( 0, len(groceries)):
        print(groceries[row][column], end="        ")
    print()
    
#2d list are like 2 dimension arrays in other languages , beasically its made of individual list