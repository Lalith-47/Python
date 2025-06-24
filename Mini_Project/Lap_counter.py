from datetime import datetime
from pprint import pprint
laps={}
start = datetime.now()
print(f"Click Enter to record lap and type 'exit' to stop Lap count")
i=1
while True:
    if 'exit'!= input().lower():
        lap=(datetime.now()-start).total_seconds()
        print(f"Lap {i}: {lap:.2f}")
        laps[f"Lap {i}"]=f"{lap:.2f}"
        i+=1
    else:
        break
stop=datetime.now()
laps[f"Total time"]=f"{(stop-start).total_seconds():.2f}"
pprint(laps)