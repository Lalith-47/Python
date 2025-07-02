import json,pprint,sys
student={
    "Basic info": {"Name": None,"reg_no": None,"dob": None,"gender": None,"email":None,"phone": None},
    "Academics":{"branch": None,"sem": None,"section": None,"cgpa": None,"backlogs": None},
    "marks": {"Python": 85,"C Programming": 78,"Maths": 90 },
    "skills": {"Technical": None,"Hobby": None}
}
try:
    print(f"Enter details for a student")
    for data,metadata in student.items():
        for key,value in metadata.items():
            student[data][key]=input(f"Enter {key}: ")
    print(f"Note: Student data will be saved in student json file |student_database.json |")
    with open("Student_database.json","r") as f:
        json.dump(student,f,indent=4)
    with open("Student_database.json","r") as f:
        content=json.load(f)
        pprint.pprint(content)
except Exception as f:
    print(f"Error: {str(f)}\nError at Line: {sys.exc_info()[2].tb_lineno}")