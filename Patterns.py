def pattern(a,b):
  for i in range(a+1):
      print(i*str(b))
a=int(input('Enter number of lines: '))
b=input('What to be printed? ')
pattern(a,b)