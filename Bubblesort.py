a=[]
n=int(input('Enter number of elements: '))
for i in range(0,n):
    a.append(int(input()))
for j in range(0,n):
    for j in range(0,i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)