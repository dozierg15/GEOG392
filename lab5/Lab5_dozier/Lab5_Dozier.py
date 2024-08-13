# Importing Arcpy and overwriting the environment 

import arcpy
arcpy.env.overwriteOutput = True

# Declaring a few variables to  make it easier within the rest of the code
Lab4GDB = r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb"
Structures = Lab4GDB + r"\Structures"

# creating inputs for the building number and buffer distance
building_num = int(input("Enter a building number: "))
buff_dist = int(input("Enter a buffer distance: "))

# where clause variable for the building number
where_clause = "Bldg = '%s'" % building_num

#creating a search cursor and actually checking to see if the building is there
scurs = arcpy.SearchCursor(Structures, where_clause=where_clause)
canProceed = False

for row in scurs:
    if row.getValue("Bldg") == building_num:
        canProceed = True

if canProceed == True:
    arcpy.Select_analysis(
        Structures,
        Lab4GDB + "\Structures_building_%s" % (building_num)
    )

    arcpy.Buffer_analysis(
        Lab4GDB + "\Structures_building_%s" % (building_num),
        Lab4GDB + "\Structures_building_%s" % (building_num, str(buff_dist)),
        buff_dist
    )

    arcpy.Intersect_Analysis(
        [
            Lab4GDB + "\Structures_building_%s" % (building_num, str(buff_dist)),   
            Lab4GDB + "\Structures"
        ],

        Lab4GDB + "\Structures_building_%s_intersect" % (building_num, str(buff_dist)),
        "All"
    )


