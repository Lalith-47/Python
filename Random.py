import random
a=random.randint(1,20)
for i in range(6):
    if i==5:
        print('\nMaximum limit reached\n')
        break
    print('\nAttempt: '+str(i+1))
    b=int(input('Enter a number: '))
    if a==b:
        print('Number Matched')
        break
    elif b>a:
        print('Number is high')
    else:
        print('Number is less')