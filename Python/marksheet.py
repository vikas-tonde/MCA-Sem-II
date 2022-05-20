m=[]
def getGrade(total):
    if total>=70:
        return "dist"
    elif total>=60: 
        return "A"
    elif total>=50:
        return "B"
    elif total>=40:
        return "pass"

def checkResult(marks):
    if marks<40:
        return False
    return True

n= int(input("Enter the number of students: "))
data=[]

for i in range(n):
    s=[]
    s.append(input(f'Enter the name of the student {i+1}: '))
    s.append(int(input(f'Enter the marks for subject 1 of the student {i+1}: ')))
    s.append(int(input(f'Enter the marks for subject 2 of the student {i+1}: ')))
    s.append(int(input(f'Enter the marks for subject 3 of the student {i+1}: ')))
    s.append(int(input(f'Enter the marks for subject 4 of the student {i+1}: ')))
    data.append(s)

print("No.\t Name\t M1\t M2\t M3\t M4\t Total\t result\t %\t Grade")
for  i in range(n):
    s=data[i]
    total=sum(s[1:])
    passed = True
    for m in s[1:]:
        if not checkResult(m):
            passed=False
            break
    percentage="-"
    grade="-"
    result='fail'
    if passed:
        percentage =(total/400)*100
        result="pass"
        grade= getGrade(percentage)
    print(f"{i+1}\t {s[0]}\t {s[1]}\t {s[2]}\t {s[3]}\t {s[4]}\t {total}\t {result}\t {percentage}\t {grade}")

    