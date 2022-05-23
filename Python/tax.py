amt= int(input("Enter the amount: "))
age= int(input("Enter the age: "))

if(amt>1000000):
    print("Tax amount is: ",(30*amt)/100)
elif(500000<amt<=1000000):
    print("Tax amount is: ",(20*amt)/100)
elif(300000<amt<=500000 and age<80):
    print("Tax amount is: ",(5*amt)/100)
elif(250000<amt<=300000 and age<60):
    print("Tax amount is: ",(5*amt)/100)
else:
    print("Relax! you don't need to pay any tax")
