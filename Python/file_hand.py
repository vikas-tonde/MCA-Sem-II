import re

n = int(input("Enter the how many numbers: "))
with open("nums.txt", 'w') as f:
    for i in range(n):
        f.write(input(f"Enter the number {i+1}: ")+" ")

f = open("nums.txt", "r")
lines = f.read()
f.close()
lines = re.split("\s", lines)
lines = lines[0:len(lines)-1]
odd = open("odd.txt", 'w')
even = open("even.txt", 'w')
for line in lines:
    if int(line) % 2 == 0:
        even.write(line+"\n")
    else:
        odd.write(line+"\n")
odd.close()
even.close()

print("Original File content: ")
with open("nums.txt", 'r') as f:
    print(f.read())

print("Odd File content: ")
with open("odd.txt", "r") as f:
    print(f.read())

f= open("odd.txt", "r")
odds=f.readlines()
f.close()
f= open("odd.txt", "a+")
s = 0

for i in odds:
    s += int(i)
f.write("\nSum is: "+str(s))
f.close()

print("Even File content: ")

with open("even.txt", "r") as f:
    print(f.read())

f= open("even.txt", "r")
evens=f.read()
evens=re.split("\s",evens)
f.close()
f=open("even.txt", "a+")
s = 0
for i in evens:
    if(i!=''):
        s += int(i)
f.write("\nSum is: "+str(s))
f.close()

print("Odd File content: ")
with open("odd.txt", "r") as f:
    print(f.read())

print("Even File content: ")
with open("even.txt", "r") as f:
    print(f.read())
