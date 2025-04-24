def prime():
    n=int(input('Enter the value: '))
    pas='True'
    for i in range(2,n):
        if n%i==0:
            pas='False'
    if pas=='True':
        print(n,'is a prime number')
    else:
        print(n,'is not a prime number')
            
prime()