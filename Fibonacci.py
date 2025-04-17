def fibo(i):
    if i <= 1:
        return i
    else:
        a=0
        a = (fibo(i-1)+fibo(i-2))
        return a
n=int(input('Enter value: '))
for i in range(0,n+1):
    print(fibo(i),end=' ')