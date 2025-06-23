from datetime import date
current_date = date.today()
d,m,y = input("Enter future date in dd-mm-yyyy format: ").split('-')
d,m,y=int(d),int(m),int(y)
try:
    future_date = date(y,m,d)
    diff = future_date - current_date
    if diff.days > 0:
        print(f"{diff.days} days left")
    elif diff.days == 0:
        print(f"Entered date is today")
    else:
        print(f"You Entered past date which was before {-1 * diff.days} ago")
except:
    print(f"Date {y}-{m}-{d} is not valid")