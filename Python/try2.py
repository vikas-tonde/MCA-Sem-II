import random
n = int(input("Guess the number: "))
a= random.randint(0,9)
if n==a:
    print("The number was",a)
    print("You won")
else:
    print("The number was",a)
    print("You lost")