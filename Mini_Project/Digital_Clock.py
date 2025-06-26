from datetime import datetime
import time
while True:
    date=datetime.now()
    time.sleep(1)
    print(date.strftime("Date: %d-%m-%Y   Time: %I:%M:%S %p"),end='\r',flush=True)