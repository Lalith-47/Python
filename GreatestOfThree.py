a=[]
n=int(input('Enter number of values to be entered'))
print('Enter values')
for i in range(0,n):
    a.append(int(input()))
print(a)
max=0
for i in a:
    if i>max:
        max=i

print('max: ',max)