# we going to import time, then simulate a  count down timer

import time 

starting_point=int(input("Choose any number as a starting point for a count down"))

while starting_point >= 0:
    time.sleep(3)
    print(starting_point)
    starting_point-=1
print("Time is up nigga")