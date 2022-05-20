
m1 = []
m2 = []

def updateMachines(data, status):
    for i in data.keys():
        if i not in status:
            global m1, m2
            m1.append(data[i][0])
            m2.append(data[i][1])


m = int(input('Enter the number of machines: '))
n = int(input('Enter the number of jobs: '))

data = {}
# letters= list(map(chr, range(97,123)))
for i in range(n):
    jobTitle = input('Enter the job title: ')
    a = (int(input(f"Enter the job time for machine 1 for job {jobTitle}: ")))
    b = (int(input(f"Enter the job time for machine 2 for job {jobTitle}: ")))
    m1.append(a)
    m2.append(b)
    data[jobTitle] = [a, b]

print("Job", f"m1    m2")
for i in data.keys():
    print(i, f"   {data[i][0]}    {data[i][1]}")

seq = [0 for i in range(n)]
left = 0
right = n-1
status = []
for i in range(n):
    min1 = min(m1)
    min2 = min(m2)
    job = 0
    if(min1 < min2):
        # if time of machine 1 is less
        if m1.count(min1) > 1:
            o = m1.count(min1)
            minIndex = m1.index(min1)
            for i in range(o-1):
                i2 = m1.index(min1, minIndex+1)
                minIndex = minIndex if m2[minIndex] <= m2[i2] else i2
            job = data.keys()[minIndex]
        else:
            job = data.keys()[m1.index(min1)]
        seq.insert(left, job)
        left = left + 1
        status.append(job)
        updateMachines(data, status)
    elif min1 > min2:
        # If time of machine 2 is less
        if m2.count(min2) > 1:
            o = m2.count(min2)
            minIndex = m2.index(min2)
            for i in range(o-1):
                i2 = m2.index(min2, minIndex+1)
                minIndex = minIndex if m1[minIndex] <= m1[i2] else i2
            job = data.keys()[minIndex]
        else:
            job = data.keys()[m2.index(min2)]
        seq.insert(right, job)
        right = right - 1
        status.append(job)
    else:
        # in case both are same
        pass
