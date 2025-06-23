from datetime import datetime, timedelta
laps={}
Initial_start=datetime.now()
i=1
print(f"Press enter to record lap and to stop enter exit")
while True:
    x=0
    if "exit" != input('\r').lower():
        x = f'{(datetime.now() - Initial_start).total_seconds():.2f}'
        laps[f"Lap {i}"] = x
        print(f"Lap {i}: {x}")
        i += 1
    else:
        break
Final_stop=datetime.now()
laps["Total lap"]=f'{(Final_stop-Initial_start).total_seconds():.2f}'
print(laps)