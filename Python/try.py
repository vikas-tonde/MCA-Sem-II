def binaryToDecimal(num):
    num= num[::-1]
    ans=0
    for i in range(len(num)):
        ans+=(2**i)*int(num[i])
    return ans

print(binaryToDecimal(str(1010)))