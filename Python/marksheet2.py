names=[]
sub1=[]
sub2=[]
sub3=[]
sub4=[]
total=[]
result=[]
percentage=[]
grade=[]

for i in range(2):
    names.append(input('Enter the name of the student: '))
    sub1.append(int(input("Enter the sub 1 marks: ")))
    sub2.append(int(input("Enter the sub 2 marks: ")))
    sub3.append(int(input("Enter the sub 3 marks: ")))
    sub4.append(int(input("Enter the sub 4 marks: ")))

print("No.\t Name\t Sub1\t Sub2\t Sub3\t Sub4\t Total\t Result\t %\t Grade")
for i in range(2): 
    total.append(sub1[i]+sub2[i]+sub3[i]+sub4[i])
    percentage.append(float(total[i]/4))
    if(int(percentage[i])>=70):
        grade.append("Dist")
    elif(int(percentage[i])>=60):
        grade.append("A")
    elif(int(percentage[i])>=50):
        grade.append("B")
    elif(int(percentage[i])>=40):
        grade.append("C")
    else:
        grade.append("F")
    result.append("Pass")
    if(sub1[i]<35 or sub2[i]<35 or sub3[i]<35 or sub4[i]<35):
        result[i]="fail"
        percentage[i]="-"
        grade[i]="-"
    print(i+1,"\t",names[i],"\t",sub1[i],"\t",sub2[i],"\t",sub3[i],"\t",sub4[i],"\t", total[i],"\t",result[i],"\t",percentage[i],"\t", grade[i])
