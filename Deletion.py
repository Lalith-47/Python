n=int(input('Enter Number of Elements to be entered: '))
a=[]
for i in range(n):
    a.append(int(input()))
print(len(a))
index=int(input('Enter index: '))
a=a[:index]+a[index+1:]
print(a)
