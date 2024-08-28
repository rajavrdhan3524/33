name=input("enter your name: ")
print(name)
print("wellcome to quiz game")

import random
x= random.randint(1,100)
y= random.randint(1,100)
y=y*y

x1=random.randint(x,y)
user_number = int(input(f"enter a square of {x1}\n"))
while user_number !=x1*x1:
    print("enter again....")
    user_number = int(input(f"enter a square of {x1}\n"))

user_number = int(input(f"enter a squareroot of {y}\n"))   
                       
    