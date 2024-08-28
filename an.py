# import random
# x= random.randint(1,100)

# name=input("enter your name: ")
# print(name)
# user_number = int(input(f"enter a square of {x}\n"))

# if user_number ==x*x:
#     print("square is coorect")

# else:
#     print("square is wrong")


import random
x= random.randint(1,100)

user_number = int(input(f"enter a square of {x}\n"))

while user_number !=x*x:
    print("enter again....")
    user_number = int(input(f"enter a square of {x}\n"))


print("square is coorect")