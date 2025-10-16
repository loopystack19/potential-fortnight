**Conditional expressions in python**
- For someone who has experience in js , i would say that conditional expressions are an equivalent to ternary operator, they are a short form of if-else statements

**Traditional use of if-else statements can sometimes be long and tideous**

-sample programme

a=12

b=34

if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")

**When can replace this with:**

a=12

b=34

print(f"{a} is greater than {b}" if a> b else f"{b} is greater than {a}")

**This is makes our code easier to read and shorter to write, therefore it becomes more efficient**