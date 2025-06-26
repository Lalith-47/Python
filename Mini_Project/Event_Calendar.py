import calendar , sys
try:
    y=int(input(f"Enter year(YYYY): "))
    m=int(input(f"Enter month(MM): "))
    Event_Month=calendar.monthcalendar(y,m)
    Events={}
    n=int(input(f"Enter Number of Events: "))
    for _ in range(n):
        event_date=int(input(f"Enter Event date: "))
        desc=input(f"Enter Description: ")
        Events[event_date]=desc
    CompleteWeek=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    CompleteWeek='   '.join(CompleteWeek)
    print('\n')
    print(f"🗓️ {calendar.month_name[m]} {y}".rjust(25))
    print(CompleteWeek)
    for week in Event_Month:
        line=''
        for day in week:
            if day==0:
                line+='      '
            elif day in Events.keys():
                line+=str(day).zfill(2)+'*   '
            else:
                line+=str(day).zfill(2)+'    '
        print(line)
    for date,desp in Events.items():
        print(f"\nDate: {date}\nDescription: {desp}")
except Exception as e:
    exc_type, exc_obj, tb = sys.exc_info()
    tb = tb.tb_lineno
    print(f"Error: {e} \nError in Line: {tb}")
finally:
    print(f"Code Execution Completed")