from datetime import datetime, timezone, timedelta,date
curr=date.today()
months_of_year=[31,28,31,30,31,30,31,31,30,31,30,31]
try:
    print(f"Calculations will be done based on 365 days 12 months and 30 days")
    d,m,y=input(f"Enter date in dd-mm-yyyy format: ").split('-')
    print(f"Current date: {date.today()}")
    fu=date(int(y),int(m),int(d))
    mon=months_of_year[int(m)-1]
    print(mon)
    if fu>=curr:
        tot=(fu-curr).days
        day=tot
        year=0;month=0
        if tot <=30:
            print(f"No of Days Left: {tot} ")
        elif 30 < tot < 365:
            month=tot//mon
            tot=tot%mon
            print(f"No of Days Left: {month} months {tot} days ")
        else:
            year=day//365
            month=day%365
            if month>12:
                month = month // mon
                day = month % mon
            if month==0:
                print(f"No of Days Left: {tot}\n{year} years")
            elif 0 > month > 11:
                print(f"No of Days Left: {tot}\n{year} years {month} months")
            else:
                print(f"No of Days Left: {tot}\n:{year} years {month} months {day} days ")


    else:
        print(f"Invalid date")
except Exception as e:
    print(f"Error: {e}")
finally:
    print(f"Code execution completed")