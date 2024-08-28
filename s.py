import random
name=input("enter your name :\n")
print("welcome to the game",name)
while (True):
    x=random.randint(1,100)
    option=random.randint(1,2)
    if(option==1):
        print("what a square of :\n",x)
        print("code for square: ")
        ans=input()
        while user_number !=x*x:
            print("enter again....")
            user_number = int(input(f"enter a square of {x}\n"))
        print("Square is currect..!")

    else:
        print("code for squareroot: ")
    a=input("do you want to continue (Yes or No) ")
    if(a.lower()=="no"):
        break
