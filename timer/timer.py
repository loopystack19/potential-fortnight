#let me try build a simple timer , more of a count down simulation
import time

my_time=int(input("Enter the amount of time you need in seconds: "))

for counter in range(my_time, 0 , -1):
    seconds= counter % 60
    minutes= int((counter / 60)) % 60
    hours= int(counter / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
    

