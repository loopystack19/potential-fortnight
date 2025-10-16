**for loops**
-unlike while loops that can run infinitely, for loops only run for a finite  number of times

**sample programme**-A programme to print all numbers between 0 and 10

for counter in range(0,11):
    print(counter)

**output**
0
1
2
3
4
5
6
7
8
9
10

when using either for loop or while loops, we can use the key words continue or break

**when the key word continue is used we skip over an iteration**

--sample programme--

for counter in range(0,20):
   if counter == 13:
       continue
   else:
       print(counter)

**output**
0
1
2
3
4
5
6
7
8
9
10
11
12
14
15
16
17
18
19

**if you use the key word break, we literally break out of the loop entirely**

--sample programme---

for counter in range(0,20):
   if counter == 13:
       break
   else:
       print(counter)

**output**

0
1
2
3
4
5
6
7
8
9
10
11
12