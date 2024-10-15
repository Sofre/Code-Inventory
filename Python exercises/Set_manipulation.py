space  = ''
print(space)


set_colors={}
set_colors={'green','red','blue'}
print(set_colors)
print(space)
print("Is white in the set? ")
print(space)
for i in set_colors:
    if(i == "white"):
        print("True")
        break
    else:
       print("False")
       break




space  = ''



print("The current lenght of the set: ")

print(format(len(set_colors)))
print(space)

new_set={}
new_set =  set_colors.copy()
new_set.add("white")
new_set.add("yellow")
print(f"New set of colors:{new_set}")
print(space)
print(format(new_set.difference(set_colors)))
print(space)
new_set.remove("yellow")
print("Remove the color from the new set: ",new_set)
print(space)
print("Union set: ",format(new_set.union(set_colors)))
print(space)