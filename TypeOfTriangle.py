print('Enter 3 sides of a triangle')
a=int(input())
b=int(input())
c=int(input())
if ((a+b>c) and (b+c>a) and (a+c>b)):
    print('Its a valid triangle')
    if(a==b==c):
        print('Equilateral triangle')
    elif (a==b or b==c or a==c):
        print('Isoceles triangle')
    else:
        print('Scalene triangle')
else:
    print('Invalid triangle')