def mark_attendance(presentries,student_name,present):
    if student_name in presentries:
        presentries[student_name].append(present)
    else:
        presentries[student_name] = [present]

def striked_out(presentries):
    for student,attendance in presentries.items():
        
        absences = attendance.count(False)
        if absences==3:
           print(f"Issued warning  to ! {student}")
        elif absences>=6:
           print(f"{student} is Expelled!!")


student_presentries = {}
mark_attendance(student_presentries,'Ana',True)
mark_attendance(student_presentries,'Ana',True)
mark_attendance(student_presentries,'Mark',False)
mark_attendance(student_presentries,'Ana',True)
mark_attendance(student_presentries,'Ana',True)
mark_attendance(student_presentries,'Mark',False)
mark_attendance(student_presentries,'Ana',False)
mark_attendance(student_presentries,'Ana',False)
mark_attendance(student_presentries,'Mark',False)
mark_attendance(student_presentries,'Ana',False)

print(student_presentries)
striked_out(student_presentries)
