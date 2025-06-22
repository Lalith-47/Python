import time
from time import strftime

n=int(input('Enter timer to stop: '))
for i in range(n,-1,-1):
    time.sleep(1)
    print(f"{i} seconds lest",end='\r',flush=True)
print(f"Timer Stopped at {strftime("%I:%M:%S %p",time.localtime())}")