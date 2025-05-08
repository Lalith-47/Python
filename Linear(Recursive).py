def Linear(list,index,key):
    if index<len(list):
        if list[index]==key:
            print('Element found at index',index)
        else:
            Linear(list,index+1,key)
    else:
        print('Element not found')
list=[1,3,5,7,9,0,8,6,4,2]
index=0
key=int(input('Enter key: '))
print(list)
Linear(list,index,key)