# def even(n):
#     i=1
#     while i<=n:
#         yield i
#         i+=1

# k= int(input("Enter the number: "))
# e=[]
# o=[]
# for i in even(k):
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)

# print("Even numbers are: ",e)
# print("Odd numbers are: ",o)

# series of even
# series of odd
# series of fibonacci series
# series of squares
# series of palindrome

# a=[1,5,8,9]
# a=(2,6,7,9,0)
# a={
#     "name":"Vikas",
#     "age":24
# }
# for i in a:
#     print(a[i])

#tuple and list
# for i in a:
#     print(i)

# def gen():
#     i=1
#     while i<=3:
#         yield i
#         i+=1

# a=gen()
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# n= int(input("Enter the number of students:"))
# s=[]
# a={}
# for i in range(n):
#     a["Name"]=input("Enter the name: ")
#     a["age"]=input("Enter the age: ")
#     a["gender"]=input("Enter the gender: ")
#     s.append(a)

# for i in s:
#     print(i)


n = int(input("Enter the number of students:"))
s = {}
for i in range(n):
    a = {}
    a["Name"] = input("Enter the name: ")
    a["age"] = input("Enter the age: ")
    a["gender"] = input("Enter the gender: ")
    s[i] = a

for i in s:
    print(s[i])
