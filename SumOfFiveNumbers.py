values=[]
print('Enter 5 numbers')
Sum=0
for i in range(0,5):
    values.append(int(input()))
for i in values:
    Sum+=i
print('Sum',Sum)