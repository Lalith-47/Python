def pattern(rows):
    for i in range(rows+1):
        for j in range(rows-i):
            print(" ",end="")
        for j in range(i*2-1):
            print("*",end="")
        print()
    for i in range(rows,0,-1):
        for j in range(rows-i):
            print(" ",end="")
        for j in range(i*2-1):
            print("*",end="")
        print()
rows=int(input('Enter no of rows: '))
pattern(rows)
