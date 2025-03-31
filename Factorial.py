def fact(a):
    if  a<=1:
        return a
    return a*fact(a-1)

a=int(input("Enter the value: "))
print('Factorial of',a,'is' ,fact(a))