def palin(s):
    rev=''
    for i in s:
        rev=i+rev
    if rev==s:
        return 'True'
    else:
        return 'False'
s=input('Enter String: ')
s=s.lower()
print(palin(s))
