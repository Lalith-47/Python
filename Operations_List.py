a=[]
def add():
    n=int(input('Enter size of the list: '))
    for i in range(n):
        a.append(int(input()))
    print('List: ',a)
def remove():
    remove=int(input('\nEnter element to remove: '))
    a.remove(remove)
    print('List after removing:',a)
def update():
    index=int(input('\nEnter index to update the element: '))
    value=int(input('Enter value: '))
    a[index]=value
    print('After updation: ',a)
def sort():
    a.sort()
    print(a)
def max_min():
    print('\nMax:',a[0],'Min:',a[-1])
def main():
    add()
    remove()
    update()
    sort()
    max_min()
main()
