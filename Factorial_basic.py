n=int(input('Enter number: '))
if n<0:
    print('Enter valid number')
elif n==0:
    print('Factorial of 0 is 1\n')
else:
    a=1
    for i in range(n,0,-1):
        a=a*i
    print(a)