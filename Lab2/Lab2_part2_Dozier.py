#[---------]
# QUESTION 2

#defining function in order to add all the iterms within the list
def List2addition(part2List) :
    intitial2= 1
    for x in part2List:
         intitial2 = intitial2 + x
    return intitial2

     
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

print(List2addition(part2))