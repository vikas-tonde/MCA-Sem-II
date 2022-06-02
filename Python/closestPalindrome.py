#abd = aba find nearest palindrome
from math import ceil

def makePalindrome(val):
    val = str(val)
    if(val == val[::-1]):
        print("Given value is palindrome")
    else:
        a = val[:len(val)//2]
        print(val[:ceil(len(val)/2)], a[::-1], sep="")


val = input("Enter the string: ")
makePalindrome(val)
