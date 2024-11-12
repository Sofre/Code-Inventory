def add_grade(gradebook,studen_name,grade):
       if studen_name in gradebook:
              gradebook[studen_name].append(grade)
       else:
            gradebook[studen_name] = [grade]



def score_to_grade(gradebook):
      
      total_grades = 0
      total_students = 0

      for grades in gradebook.values():
        total_grades += sum(grades)
        total_students +=len(grades)

    
        if total_students > 0:
           average = total_grades / total_students
           return average
        else:
             return 0 

def letter_grade(avg):
      
      if 90<=avg and avg<=100:
            return 'A'
      elif 80<=avg and avg<=89:
            return 'B'
      elif 70<=avg and avg<=79:
            return 'C'
      elif 60<=avg  and avg<=69:
            return 'D'
      else:
            return 'F'



    




gradebook = {}
add_grade(gradebook,'Ana',85)
add_grade(gradebook,'Ana',90)
add_grade(gradebook,'Ana',88)
add_grade(gradebook,'Bojan',78)
add_grade(gradebook,'Filip',92)
average = score_to_grade(gradebook)
lettergrade = letter_grade(average)
print(f"Gradebook:{gradebook}")
print(f"Class avarage: {average:.1f}")
print(f"Letter grade: {lettergrade}")



