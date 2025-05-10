n=int(input('Enter the size: '))
ele=int(input('Enter the search Element: '))
low=0
high=n-1
a=[]
pas=0
for i in range(n):
    a.append(int(input('Element '+str(i+1)+': ')))
a.sort()
print(a)
while low<=high:
    mid=((low+high)//2)
    if a[mid]==ele:
        print('Element found at index',mid)
        pas=1
        break
    elif a[mid] < ele:
        low = mid + 1
    elif a[mid] > ele:
        high = mid - 1
    
if pas==0:
    print('Element not found')

