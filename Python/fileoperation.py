import os
folder = input("Enter the folder name: ")
path = "./"+folder+"/"

if os.path.exists(folder):
    lstFile = os.listdir(folder)
    os.chmod(folder, 0o777)
    for i in lstFile:
        os.remove(path+i)
    os.rmdir(folder)

os.mkdir(folder)
name = input("Enter the file name: ")
f = open(path+name, "w")
n = int(input("Enter the number of lines you want to write: "))
for i in range(n):
    f.write(input(f"Enter the content of line {i+1}:")+"\n")
f.close()
f = open(path+name, "r")
fc = open(path+"copy.txt", "w+")
fc.write(f.read())
f.close()
fc.close()
rn = input("Enter the copied file name: ")
os.rename(path+"copy.txt", path+rn)
f = open(path+name, "r")
# print(f.read().split(/[\s]/))
f.close()
