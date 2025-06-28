import csv
file_name=input(f"Enter File name: ")
with open(file_name,"a+",newline="") as f:
    data = csv.writer(f)
    data.writerow(["name","reg no","city","marks"])
    n=int(input(f"Enter No of students: "))
    for i in range(n):
        name,reg_no,city,marks=input(f"Enter Name,Reg No,City,Marks in a single line seprated by space: ").split()
        data.writerow([name,reg_no,city,marks])