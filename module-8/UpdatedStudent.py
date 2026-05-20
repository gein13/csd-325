#Scott Chamberlain
#CSD325 M8.2 Assignment
#5/18/2026 (late)

import json

def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

with open(r"c:\Users\sjcha\csd\csd-325\module-8\student.json", "r") as file:
    students = json.load(file)

print() #Add a space for legibility
#6c. Output notification to the user that this is the original Student list.
print("This is the original Student list.")
#6d. Call your print function.
print_students(students)

#6e. Add your last name, first name, fictional ID, and email to the class list using append().
students.append({
    "L_Name": "Chamberlain",
    "F_Name": "Scott",
    "Student_ID": 21414883,
    "Email": "schamberlain@my365.bellevue.edu"
})

#6f. Output notification to the user that this is the updated Student list.
print("\nThis is the updated Student list.")
#6g. Call your print function.
print_students(students)

#6h. Use the JSON dump() function to append the new data to the .json file.
with open(r"c:\Users\sjcha\csd\csd-325\module-8\student.json", "w") as file:
    json.dump(students, file, indent=4)

#6i. Output notification to the user that the .json file was updated.
print("\nThe student.json file was updated.")