import sys
n=int(input('Enter number of elements: '))
print('Enter the elements')
a=[]
for i in range(n):
    a.append(int(input()))
print(a)
print('Do you want to insert or delete any value?\nIf Yes Enter y\nIf No Enter n')
do=input()
do=do.lower()
if do =='n':
    print('Program terminated')
    sys.exit(0) 
elif do=='y':
    WantTo=int(input('Enter \n1 to Insert\n2 to delete\n'))
    if WantTo==1:
        index=int(input('Enter at what index to be inserted: '))
        value=int(input('Enter value: '))
        a.insert(index,value)
        print(a)
    elif WantTo==2:
        delete=int(input('Enter Element to be deleted: '))
        a.remove(delete)
        print(a)
    else:
        print('Invalid Input')
        sys.exit(0)
else:
    print('Invalid Input')   
    sys.exit(0)

