def add_grade(gradebook,student_name,grade):
    if student_name in gradebook:
        gradebook[student_name].append(grade)
    else:
        gradebook[student_name] = [grade]


def sorting_by_grade(gradebook):
   
   for student,grades in gradebook.items():
       sorting(grades)
      
       
def searching_by_grade(gradebook,item):
    found = False
    for  student_name,grades in gradebook.items():
        if search(grades,item):
            found = True
            print(f"Found {student_name}'s grade {item} ")
        if not found:
            found = False
            print(f"Did not find {student_name}'s grade {item} ")




#bubble sort
def sorting(list):
    for outter_loop in range(len(list)-1,0,-1):
        for i in range(outter_loop):
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
#linear search
def search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return True
    return False

       


gradebook = {}
add_grade(gradebook,'Ana',100)
add_grade(gradebook,'Ana',92)
add_grade(gradebook,'Ana',94)

sorting_by_grade(gradebook)
print(gradebook)
searching_by_grade(gradebook,100)