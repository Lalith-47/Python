import csv , sys

sys.path.append("C:\\Users\\Lalit\\OneDrive - Nitte Meenakshi Institute Of Technology\\Documents\\GitHub\\Python\\Mini_Projec")
old_file=input(f"Enter old file name: ")+'.csv'
new_file=input(f"Enter new file name: ")+'.csv'
try:
    with open(old_file,"r",newline="") as f:
        data=csv.reader(f)
        with open(new_file, "a", newline="") as f2:
            new=csv.writer(f2)
            for row in data:
                new.writerow(row)
except Exception as e:
    print(f"Error Line: {sys.exc_info()[2].tb_lineno}\nError Message: {e}")