# Write a program to print all prome numbers from given r}ange.

from pip import main


def isPrime(n):
    for i in range(2, n//2):
        if(n % i == 0):
            return False
    return True


def printPrime(start, stop):
    print(f"Prime numbers between {start} to {stop}: ")
    for i in range(start, stop):
        if isPrime(i):
            print(i, end=",")


if main:
    start = int(input("Enter the start: "))
    stop = int(input("Enter the end: "))
    printPrime(start, stop)