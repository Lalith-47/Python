import datetime , sys
dt=datetime.datetime.now()
initial = datetime.datetime(1970,1,1,0,0,0)
time1 = initial;time2 = initial
def begin():
    global time1
    time1 = datetime.datetime.now()
def end():
    global time2
    time2 = datetime.datetime.now()
    datetime

def enter(log_no, message="Entry of usage of of file"):
    global time1,time2
    try:
        if time1 == initial or time2 == initial:
            print("Begin or end was not called")
        else:
            with open("log.md",'a') as f:
                f.write(
                        f"Log No: {log_no}\n"
                        f"{dt.strftime('Log Date: %d-%m-%Y Time: %I:%M:%S %p')}\n"
                        f"log Message: {message}\n"
                        f"Time taken: {(time2-time1).total_seconds():.3f}\n"
                        f"File Name: {sys.argv[0].split('\\')[-1]}\n"
                        f"File Path: {sys.argv[0]}\n\n"
                    )
    except Exception:
        print(
              f"Error line: {sys.exc_info()[2]}\n"
              f"Error Type: {sys.exc_info()[0]}\n"
              f"Error Message: {sys.exc_info()[1]}"
        )
    else:
        print(f"No Error")
    finally:
        time1 = initial
        time2 = initial
        print(f"Code Executed")