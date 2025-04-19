import random
username='Alice'
password='abc123'
OTP=random.randint(111111,999999)
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
    print('OTP: ',OTP)
    otp=int(input('Enter the OTP: '))
    if otp!=OTP:
        print('Incorrect OTP')
        continue

    if a==username and b==password and otp==OTP:
        print('Access approved ')
        break
    
