import re

m = input("Enter the main string: ")
x = re.split('\s', m)
print("Number of words are ", len(x))
x = re.findall('\d', m)
sum = 0
for i in x:
    sum += int(i)
print("Sum of the numbers is ", sum)

sym = 0
for i in m:
    if not i.isdigit() and not i.isalpha() and not i.isspace():
        sym += 1
print("Symbols: ", sym)
