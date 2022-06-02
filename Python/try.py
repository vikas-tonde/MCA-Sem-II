a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = a+b


def addition(a, b):
    print(str(a), "+", str(b), "=", str(a+b))


def check(c):
    if(c > 0):
        print("Number is positive")
    elif(c < 0):
        print("Number is negative")
    else:
        print("Number is 0")


def printUpto(c):
    for i in range(3, c+1):
        print(i)


""" k = [] #k=0
for i in range(1, 11):
    for j in range(1, c+1):
        if((i*j) % 3 == 0):
            print("**\t", end="")
            k.append(i*j) #k+=(i*j)
        else:
            print(i*j, "\t", end="")
    print()
print("Value of **= ", sum(k)) #print(k)
 """


def printTables(c):
    k = 0
    i = 1
    while(i <= 10):
        j = 1
        while(j <= c):
            if((i*j) % 3 == 0):
                print("**\t", end="")
                k += (i*j)
            else:
                print(i*j, "\t", end="")
            j += 1
        i += 1
        print()
    print("Value of **: ", k)


printTables(c)
