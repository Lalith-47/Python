name=input('Enter name of the student: ')
usn=int(input('Enter usn: '))
m=[]
for i in range(0,3):
    marks = int(input('Enter marks of subject ' + str(i+1)))
    m.append(marks)
sum=0
for i in range(0,3):
    sum=sum+m[i]
print('Name: ',name)
print('usn: ',usn)
print('Total marks: ',sum)
print('Percentage: ',(sum*100)/300)
count=0
for i in range(0,3):
    if m[i]>40:
        count=count+1
print('Passed in',count,'subjects')