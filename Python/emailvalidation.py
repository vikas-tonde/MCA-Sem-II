import re

# email=input("Enter the email id: ")
# regex= "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
# if re.fullmatch(regex, email):
#     print("Email is valid")
# else:
#     print("Email is not valid")

password = input("Enter the password: ")

if(len(password) < 8):
    print("Length should be more than 8 Character")
elif(re.search("[A-Z]", password) == None):
    print("Password must have atleast one character in uppercase")
elif(re.search("[a-z]", password) == None):
    print("Password must have atleast one character in lowercase")
elif(re.search("[0-9]", password) == None):
    print("Password must have atleast one numeric character")
elif(re.search("[#_,\*\$@]", password) == None):
    print("Password must have atleast one special character")
elif(re.search("\s", password) != None):
    print("Password must not contain space")
else:
    print("Password is valid")

