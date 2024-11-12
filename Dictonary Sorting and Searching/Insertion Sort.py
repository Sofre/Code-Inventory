import random
def search_engine(list):
    for outter_loop in range(1,len(list)):
        key = list[outter_loop]
        inner_loop = outter_loop - 1

        while inner_loop>=0 and list[inner_loop] > key:
            list[inner_loop+1] = list[inner_loop]
            inner_loop-=1

            list[inner_loop+1] = key







list = []

for i in range(4):
    list.append(random.randint(1,4))


print(list)
search_engine(list)
print(list)
