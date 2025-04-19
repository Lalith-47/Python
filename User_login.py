database={'Alice':'abc123','Bankai':'Zenpacto'}
import random
import sys
decision=int(input('Enter 1 for existing account\nEnter 2 to create account\n'))
if decision==1:
    username=input('Enter your username: ')
    if username not in database:
        print('Incorrect Username')
        sys.exit(1)
    password=input('Enter Password: ')
    if password!=database[username]:
        print('Invalid Password')
        sys.exit(0)
    OTP=random.randint(111111,999999)
    print(OTP)
    otp=int(input('Enter OTP: '))
    if otp!=OTP:
        print('Incorrect OTP')
    else:
        print('Access Approved')

elif decision==2:
    new_username=input('Enter new username: ')
    new_password=input('Enter New password: ')
    database[new_username]=new_password
    print('Username: ',new_username,'\nPassword: ',database.get(new_username))
else:
    print('Invalid input')
    sys.exit(1)