from datetime import datetime , timedelta
now=datetime(2025,5,15)
n=int(input(f"Enter days to increment: "))
result=now+timedelta(days=n)
print(result.strftime("%a %d %B %Y "))