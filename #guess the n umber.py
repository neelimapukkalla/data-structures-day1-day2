import random
n=random.randrange(1,100)
guess=int(input("enter any number:"))
while n!=guess:
    if guess<n:
        print("Too low")
        guess=int(input("enter number again:"))
    elif guess>n:
        print("Too High")
        guess=int(input("enter number again:"))
    else:
        break
    print("you guessed it right!!")

















































    

         
