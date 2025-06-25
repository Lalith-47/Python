from datetime import date, datetime, timedelta
d=int(input(f"Enter days you want to increase in DD format: "))
present_date=datetime.now().date()
future=present_date+timedelta(days=d)
print(future)