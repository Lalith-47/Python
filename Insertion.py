n=int(input('Enter number of elements to be entered: '))
a=[]
for i in range(n):
    a.append(int(input()))
index=int(input('Enter the location: '))
value=int(input('Enter the value: '))
a.append(0)
for j in range(n,index,-1):
    a[j]=a[j-1]
a[index]=value
print(a)