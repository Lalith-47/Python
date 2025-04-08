username='Alice'
password='abc123'
i=0
while i<=3:
    i+=1
    if i==4:
        print('Maximum limit reached ')
        break
    a=input('Enter username ')
    if a!=username:
        print('Wrong username ')
        continue 
    
    b=input('Enter password ')
    if b!=password:
        print('Invalid Password ')
        continue 
    
    if a==username and b==password:
        print('Acceass approved ')
        break
    
