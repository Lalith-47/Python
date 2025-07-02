import csv,sys
students = [
    {"Name": "John", "RegNo": "101", "Subject1": 78, "Subject2": 65, "Subject3": 88},
    {"Name": "Asha", "RegNo": "102", "Subject1": 45, "Subject2": 39, "Subject3": 50},
    {"Name": "Raj", "RegNo": "103", "Subject1": 23, "Subject2": 29, "Subject3": 33},
    {"Name": "Meera", "RegNo": "104", "Subject1": 67, "Subject2": 72, "Subject3": 70},
    {"Name": "Ali", "RegNo": "105", "Subject1": 34, "Subject2": 48, "Subject3": 41},
    {"Name": "Kiran", "RegNo": "106", "Subject1": 90, "Subject2": 91, "Subject3": 89},
    {"Name": "Divya", "RegNo": "107", "Subject1": 55, "Subject2": 59, "Subject3": 60},
    {"Name": "Sohan", "RegNo": "108", "Subject1": 38, "Subject2": 40, "Subject3": 35},
    {"Name": "Anu", "RegNo": "109", "Subject1": 85, "Subject2": 78, "Subject3": 82},
    {"Name": "Vikram", "RegNo": "110", "Subject1": 60, "Subject2": 62, "Subject3": 65},
]
try:
    #Writing adat to the file
    fieldname=["Name","RegNo","Subject1","Subject2","Subject3"]
    with open("Student_DB.csv","w",newline="") as write:
        enter=csv.DictWriter(write,fieldnames=fieldname)
        enter.writeheader()
        enter.writerows(students)
    #Updating with new values
    updated_csv_data=[]
    with open("Student_DB.csv","r",newline="") as read:
        content=csv.DictReader(read)
        for row in content:
            summed=int(row["Subject1"])+int(row["Subject2"])+int(row["Subject3"])
            average=f"{summed/3:.2f}"
            row["Total"]=summed
            row["average"]=average
            updated_csv_data.append(row)
    #Writing Updated info to the file
    fieldname+=["Total","average"]
    with open("Student_DB.csv","w",newline="") as update:
        enter=csv.DictWriter(update,fieldnames=fieldname)
        enter.writeheader()
        enter.writerows(updated_csv_data)
except FileNotFoundError as fnfe:
    print(f"Error: {str(fnfe)}\nError at line: {sys.exc_info()[2].tb_lineno}")
except Exception as e:
    print(f"Error: {str(e)}\nError at line: {sys.exc_info()[2].tb_lineno}")