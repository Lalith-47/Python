def pattern(n):
    for i in range(1,n+1):
        print('\n')
        for j in range(1,i+1):
            print(j,end=' ')
n=int(input('Enter number of lines: '))
pattern(n)