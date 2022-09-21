import re

fname=input("Enter the filename: ")
f = open(fname,'r')
text=f.read()
m=re.findall("[0-9]{10}",text)
a = re.findall("[A-Za-z0-9]+@[a-z]+\.[a-z]{2,3}",text)
with open("email.txt","w") as file:
    for i in a:
        file.write(i+"\n")
with open("mobile.txt","w") as file:
    for i in m:
        file.write(i+"\n")