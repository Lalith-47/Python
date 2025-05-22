rows=int(input('Enter rows for 1st matrix: '))
cols=int(input('Enter columns for 1st matrix: '))
a=[]
b=[]
sum=[]
for i in range(rows):
    r=[]
    for j in range(cols):
        r.append(int(input('A'+str(i+1)+str(j+1)+str(': '))))
    a.append(r)
print('A: ',a)
rows1=int(input('Enter rows for 2nd matrix: '))
cols1=int(input('Enter columns for 2nd matrix: '))
if rows!=rows1 and cols!=cols1:
    print('Dimensions mismatched ')
else:
    print('Matrix Addition possible')
   # sys.out()
    for i in range(rows1):
        s=[]
        for j in range(cols1):
            s.append(int(input('B'+str(i+1)+str(j+1)+str(': '))))
        b.append(s)
    print('B: ',b)
# !Matrix addition 
    for i in range(rows):
        x=[]
        for j in range(cols):
            add=a[i][j]+b[i][j]
            x.append(add)
        sum.append(x)
    print('Sum: ',sum)

