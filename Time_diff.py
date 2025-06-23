import time
future_date=input("(Enter in DD-MM-YYYY format)Future Date: ")
future_time = time.mktime(time.strptime(future_date, "%d-%m-%Y"))
present_time=time.time()
if future_time > present_time:
    time_period=future_time-present_time
    time_left=time.localtime(time_period)
    if  time_left.tm_year-1970 == time_left.tm_mon-1 == time_left.tm_mday == time_left.tm_hour == time_left.tm_min == 0:
        print(f" {time_left.tm_sec} seconds left")
    elif time_left.tm_year-1970 == time_left.tm_mon-1 == time_left.tm_mday == time_left.tm_hour == 0:
        print(f" {time_left.tm_min} minutes {time_left.tm_sec} seconds left")
    elif time_left.tm_year-1970 == time_left.tm_mon-1 == time_left.tm_mday == 0:
        print(f" {time_left.tm_hour} Hours {time_left.tm_min} minutes {time_left.tm_sec} seconds left")
    elif time_left.tm_year-1970 == time_left.tm_mon-1 == 0:
        print(f" {time_left.tm_mday} days {time_left.tm_hour} Hours {time_left.tm_min} minutes {time_left.tm_sec} seconds left")
    elif time_left.tm_year - 1970 == 0:
        print(f" {time_left.tm_mon} months {time_left.tm_mday} days {time_left.tm_hour} Hours {time_left.tm_min} minutes {time_left.tm_sec} seconds left")
    else:
        print(f"{time_left.tm_year - 1970} years {time_left.tm_mon - 1} months {time_left.tm_mday} days {time_left.tm_hour} Hours {time_left.tm_min} minutes {time_left.tm_sec} seconds left")
else:
    print("Future time is already passed")