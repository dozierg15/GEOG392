#  Lab 4 - Garrett Dozier - GEOG 392 (GIS Programming) - Section 501
# I did this code in Windows as opposed to Mac this time
# My code is mixed up with various route to reach the problems

import arcpy, sys
arcpy.env.overwriteOutput = True 
# setting workspace for below functions
arcpy.env.workspace = r"C:\Users\seths\Documents\Dozier\Lab4"

# ----- #
# feel free to change file paths when necessary - as it applies to your own computer - these file paths are from the data given, and used computer in CSA - also this code can be found in PPT

# ----- #
#Creating GDB - parantheses look weird but able to do so - imports csv into an event layer and creates the new GDB - as noted more earlier


arcpy.CreateFileGDB_management(
    r"C:\Users\seths\Documents\Dozier\Lab4",
    "Lab4GDB"
    )

# ----- #
#Creating XY load in - parantheses look interesting but able to do so - also variable for CSV file - used copy features to create actual outputted file
incsv = r"C:\Users\seths\Documents\Dozier\Lab4\garages.csv"
outShp = r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\garagepts"

arcpy.MakeXYEventLayer_management(
    incsv,
    "X",
    "Y",
    "garagePts"
    )
arcpy.CopyFeatures_management("garagepts",outShp)

# ----- #
#loading in the xy points as wells as previosuly created GDB above - able to check using ArcGIS Pro (should check)
arcpy.FeatureClassToFeatureClass_conversion(
    r"C:\Users\seths\Documents\Dozier\Lab4\Campus.gdb" + r"\Structures",
    r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb",
    "Structures"
    )

# ----- #
# placing the GDB from data into the newly created GDB from above


arcpy.Copy_management(
    r"C:\Users\seths\Documents\Dozier\Lab4\Campus.gdb" + r"\Structures",
    r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb" + r"\Structures"
    )

# ----- #
# adding spatial reference (projection)


spatial_ref = arcpy.Describe(
    r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb" + r"\Structures").spatialReference


# Setting newly created feature into the corrected cooridnate system/spatial reference - this is a different way than I have previsouly done (the variables...)
input_features =  r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\Structures"

# output data
output_feature_class = r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\Structures_Reprojected"

# create a spatial reference object for the output coordinate system
out_coordinate_system = arcpy.SpatialReference('NAD 1983 StatePlane Texas Central FIPS 4203 (Meters)')

# run the tool
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

# Creating the buffer and input/variable for the actual buffer distance
bufferdistance = "150 meters"

arcpy.Buffer_analysis(r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb" +r"\garagePts",
r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\Buffered_GaragePoints",
bufferdistance
)

# Intersection of Structures (Buildings) and Garages
arcpy.Intersect_analysis([r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\Structures_Reprojected", r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb" +r"\garagePts"], 
r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\Structures_Garages_Intersect",
"All"
)

#Showing the intersected tables
arcpy.TableToTable_conversion(r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\Structures_Garages_Intersect",
r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb",
"Table_Created"
)

#Showing the intersected tables - this time just into lab 4 in order to post it in github
arcpy.TableToTable_conversion(r"C:\Users\seths\Documents\Dozier\Lab4\Lab4GDB.gdb\Structures_Garages_Intersect",
r"C:\Users\seths\Documents\Dozier\Lab4",
"Table_Created.csv"
)