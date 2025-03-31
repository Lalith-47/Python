def fibo(a):
    if a==0 or a==1:
        return a
    return fibo(a-1)+fibo(a-2)

a=int(input("Enter the value: "))
for i in range(0,a+1):
    print(fibo(i))   
