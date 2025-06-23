from datetime import datetime , timedelta
now=datetime.now().date()
n=int(input(f"Enter days to increment: "))
result=now+timedelta(days=n)
print(result.strftime("%d %B %Y"))