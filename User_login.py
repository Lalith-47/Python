database={'Alice':'abc123','Bankai':'Zenpacto'}
import random
import sys
def login():
    i=0
    while i<=3:
        if i==3:
            print('Max limit reached')
            sys.exit(0)
        username=input('Enter your username: ')
        if username not in database:
            print('Incorrect Username')
        else:
            break
        i+=1
    i=0
    while i<=3:
        if i==3:
            print('Max limit reached')
            sys.exit(0)
        password=input('Enter Password: ')
        if password!=database[username]:
            print('Invalid Password')
        else:
            break
        i+=1
    i=0
    while i<=3:
        if i==3:
            print('Max limit reached')
            sys.exit(0)
        OTP=random.randint(111111,999999)
        print(OTP)
        otp=int(input('Enter OTP: '))
        if otp!=OTP:
            print('Incorrect OTP')
        else:
            print('Access Approved')
            break
        i+=1
def signup():
    while True:
        new_username=input('Enter new username: ')
        if new_username in database:
            print('Username already exists')
        else:
            break
    new_password=input('Enter New password: ')
    database[new_username]=new_password
    print('Username: ',new_username,'\nPassword: ',database.get(new_username))
def invalid():
    print('Invalid Input')
def main():
    while True:
        decision=input('Do you want to login or signup? (login/signup): ').lower()
        if decision=='login':
            login()
        if decision=='signup':
            signup()  
        else:
            invalid()
            continue
main()  