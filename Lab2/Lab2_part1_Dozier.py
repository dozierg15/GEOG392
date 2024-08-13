#[---------]
# QUESTION 1

#defining function in order to multipy all the iterms within the list
def List1multiply(part1List) :
    intitial1= 1
    for x in part1List:
         intitial1 = intitial1 * x
    return intitial1
     


part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

print(List1multiply(part1))



 