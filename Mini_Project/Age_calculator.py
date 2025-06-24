from datetime import date
d,m,y=input(f"Enter you birthday in DD-MM-YYYY format: ").split('-')
today=date.today()
bday=date(int(y),int(m),int(d))
print(f"AGE : {today.year-bday.year}\nYou are {today.year-bday.year} yrs {today.month-bday.month} months {today.day-bday.day} days old")