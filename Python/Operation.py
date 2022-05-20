while True:
    print("1.Armstrong \n2.Palindrome \n3.Perfect \n4.Prime \n5.Exit")
    n=int(input("Enter your choice: "))
    
    if n==5:
        break
    
    elif n==1:
        num=int(input("Enter the number: "))
        l=len(str(num))
        s=0
        t=num
        while num>0:
            r=num%10
            s=s+(r**l)
            num=num//10
        if t==s:
            print(f"{t} is armstrong")
        else:
            print(f"{t} is not armstrong")
    elif n==2:
        num=int(input("Enter the number: "))
        s=0
        t=num
        while num>0:
            r=num%10
            s=s*10+r
            num=num//10
        if t==s:
            print(f"{t} is Palindrome")
        else:
            print(f"{t} is not Palindrome")
    elif n==3:
        num=int(input("Enter the number: "))
        s=0
        i=1
        while num//2>=i:
            if num%i==0:
                s=s+i
            i=i+1
        if num==s:
            print(f"{num} is Perfect")
        else:
            print(f"{num} is not Perfect")
    elif n==4:
        num=int(input("Enter the number: "))
        s=0
        i=2
        flag=False
        while num//2>=i:
            if num%i==0:
                flag=True
                break
            i=i+1
        if not flag:
            print(f"{num} is Prime")
        else:
            print(f"{num} is not Prime")      
