# Write a Program to create number converter

print("Number Converter")
octal = {'0', '1', '2', '3', '4', '5', '6', '7'}
hexa = {'0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
hexValues = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
hexTable = {0: '0', 1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'A', 11: 'B',
            12: 'C', 13: 'D', 14: 'E', 15: 'F'}
deci = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def checkDecimal(num):
    for i in num:
        if i not in deci:
            return False
    return True


def checkOctal(num):
    for i in num:
        if i not in octal:
            return False
    return True


def checkHexadecimal(num):
    for i in num:
        if i.isalpha():
            i = i.lower()
        if i not in hexa:
            return False
    return True


def binaryToDecimal(num):
    num = num[::-1]
    ans = 0
    for i in range(len(num)):
        ans += (2**i)*int(num[i])
    return ans


def octalToDecimal(num):
    num = num[::-1]
    ans = 0
    for i in range(len(num)):
        ans += (8**i)*int(num[i])
    return ans


def hexaDecimalToDecimal(num):
    num = num[::-1]
    ans = 0
    for i in range(len(num)):
        a = num[i]
        if num[i].isalpha():
            a = hexValues[num[i].lower()]
        ans += (16**i)*int(a)
    return ans


def decimalToBinary(num):
    bin = ''
    while num:
        bin += str(num % 2)
        num = num//2
    print("Given number in Binary is:", bin[::-1])


def decimalToOctal(num):
    ans = ''
    while num:
        ans += str(num % 8)
        num = num//8
    print("Given number in Octal is:", ans[::-1])


def decimalToHexadecimal(num):
    ans = ''
    while num:
        ans += hexTable[num % 16]
        num = num//16
    print("Given number in hexa Decimal is:", ans[::-1])


def convertFromDecimal(num, base):
    num = int(num)
    if base == 2:
        decimalToBinary(num)
    elif base == 8:
        decimalToOctal(num)
    elif base == 16:
        decimalToHexadecimal(num)
    elif(base==10):
        print("Given number in Decimal is:",num)


while True:
    n = input("Enter the number you want to convert: ")
    currentBase = int(
        input("Select Base = \n1. Decimal \n2.Binary \n3.Octal \n4.Hexadecimal "))
    baseToConvert = int(input("Enter the base to convert: "))
    if(not currentBase == 1):
        if(currentBase == 2):
            if set(n) == {'0', '1'}:
                n = binaryToDecimal(n)
            else:
                print('Enter number is not valid binary')
                break
        elif currentBase == 3:
            if checkOctal(n):
                n = octalToDecimal(n)
            else:
                print('Enter number is not valid Octal')
                break
        elif currentBase == 4:
            if checkHexadecimal(n):
                n = hexaDecimalToDecimal(n)
            else:
                print('Enter number is not valid Hexadecimal')
                break

    if not checkDecimal(str(n)):
        print("Enter number is not valid Decimal")
        break
    convertFromDecimal(n, baseToConvert)