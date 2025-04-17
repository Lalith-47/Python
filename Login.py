username='Alice'
password='abc123'
i=0
while i<=5:
    i+=1 
    if i==6:
        print('Maximum limit reached ')
        break
    print('Attempt',i)
    a=input('Enter username ')
    if a!=username:
        print('Wrong username ')
        continue 
    
    b=input('Enter password ')
    if b!=password:
        print('Invalid Password ')
        continue 
    
    if a==username and b==password:
        print('Access approved ')
        break
    
