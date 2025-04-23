def power():
    base=int(input('Enter base: '))
    power=int(input('Enter Power: '))
    value=1
    for i in range(power):
        value*=base
    print('Output:',value)
power()