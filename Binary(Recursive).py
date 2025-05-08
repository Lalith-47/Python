def binary(list,low,high,key):
    if low>high:
        print('Element not found ')
    else:
        mid=(low+high)//2
        print(mid)
        if list[mid]==key:
            print('Element found at index',mid)
        elif list[mid]>key:
            binary(list,low,mid-1,key)
        elif list[mid]<key:
            binary(list,mid+1,high,key)
list=[2,3,7,9,6,8,9,0,5]
list.sort()
key=int(input('Enter key: '))
print(list)
binary(list,0,len(list)-1,key)