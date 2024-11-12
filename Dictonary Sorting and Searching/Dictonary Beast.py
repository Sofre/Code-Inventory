def add_grade(gradebook,student_name,grade):
    if student_name in gradebook:
        gradebook[student_name].append(grade)
    else:
        gradebook[student_name] = [grade]

def passing_values(gradebook):
    list_letter = [] 
    list_numerical = []  

    for student_name, grades in gradebook.items():
        print(f"Processing grades for {student_name}: {grades}")
        
        for grade in grades:  
            list_numerical.append(grade)
            letter_grade = grade_to_letter(grade)  
            list_letter.append(letter_grade)

        print(f"Letter grades for {student_name}: {list_letter}")
        insertion_sort(list_numerical)
        print(f"The sorted grades for {student_name} are:{list_numerical}")
        item = input("Input the grade to be looked for ")
        item = int (item)
        print(f"Looking up grade {item} for student: {student_name}")
        print("At position: ",binary_search(list_numerical,item))
        print(f"Are there good grades??")
        letter = input("Input the grade to be looked for ")
        print(linear_search(list_letter,letter))



def bubble_sort(list_numberical):
     for i in range(len(list_numberical)-1,0,-1):
          for j in range(i):
               if list_numberical[i]<list_numberical[i+1]:

                list_numberical[i],list_numberical[i+1] = list_numberical[i+1],list_numberical[i] 




def qucik_sort(list_numerical):
     if len(list_numerical)<1:
          return list_numerical
     
     pivot = list_numerical[-1]

     left = [x for x in list_numerical[:1] if x<pivot]
     right = [x for x in list_numerical[:1] if x>=pivot]

     return qucik_sort(left) + [pivot] + qucik_sort[right]
  

    

def insertion_sort(list_numerical):
     for i in range(1,len(list_numerical)):
          key = list_numerical[i]
          j = i - 1
          while j>=0 and list_numerical[j]>key:
               list_numerical[j+1] = list_numerical[j]
               j-=1
               list_numerical[j+1] = key


def selection_sort(list_numerical):
     for i in range(len(list_numerical)):
          min_index = i
          for j in range(i+1,len(list_numerical)):
               if list_numerical[j]<list_numerical[min_index]:
                    j = min_index

     list_numerical[j],list_numerical[min_index] = list_numerical[min_index],list_numerical[j]


def binary_search(list_numerical,item):
     low = 0
     high = len(list_numerical) - 1
     while low<=high:
          midpoint = (high+low)//2
          if(list_numerical[midpoint]==item):
               return midpoint
          else:
               if list_numerical[midpoint]<item:
                    low = midpoint + 1
               else:
                    high = midpoint - 1
       

def linear_search(list_letter, item):
    for pos in range(len(list_letter)):
        if list_letter[pos] == item:
            return True
    return False







def grade_to_letter(grade):
  
      
      if 90<=grade and grade<=100:
            return 'A'
      elif 80<=grade and grade<=89:
            return 'B'
      elif 70<=grade and grade<=79:
            return 'C'
      elif 60<=grade  and grade<=69:
            return 'D'
      else:
            return 'F'




gradebook = {}
add_grade(gradebook,'Dushko',85)
add_grade(gradebook,'Dushko',79)
add_grade(gradebook,'Dushko',90)
add_grade(gradebook,'Dushko',68)

print(gradebook)
passing_values(gradebook)

