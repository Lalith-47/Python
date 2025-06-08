import sys
#Defining the DAte increment function
def incrementOfDate():
    dates_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = int(input('Enter date in DD format: '))
    month = int(input('Enter Month in MM format: '))
    year = int(input('Enter Year in YYYY format: '))

    # Validate input
    if not (1 <= month <= 12) or not (1 <= date <= 31) or not (1 <= year <= 9999):
        print('Invalid data entered')
        sys.exit()

    # Check for leap year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap_year and month == 2:
        dates_in_month[1] = 29

    # Validate date against the number of days in the month
    if date > dates_in_month[month - 1]:
        print('Invalid data entered')
        sys.exit()
    # Increment date
    date += 1
    if date > dates_in_month[month - 1]:
        date = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    print(f"Next Date: {date:02d}-{month:02d}-{year}")

incrementOfDate()