import sys
def incrementOfDate():
    dates=[31,28,31,30,31,30,31,30,31,30,31,30]
    date=int(input('Enter date in DD format: '))
    month=int(input('Enter Month in MM format: '))
    year=int(input('Enter Year in YY format: '))
    if (date>0 and date<=31) and (month>0 and month<=12) and (year>0000 and year<=9999):
        pass
    else:
        print('Invalid data entered')
        sys.exit()
    if year%4==0 and year%100!=0 or year%400==0:
        pass
    elif month==2 and date>=29:
        print('Invalid data entered')
        sys.exit()
    if year%4==0 and year%100!=0 or year%400==0:
        if month==2:
            dates[1]=29
        if date==29:
            date=1
            month+=1
    date+=1
    if date>dates[month-1]:
        date=1
        month+=1
        if month>12:
            year+=1
    print(f"Next Date: {date:02d}-{month:02d}-{year}")

incrementOfDate()