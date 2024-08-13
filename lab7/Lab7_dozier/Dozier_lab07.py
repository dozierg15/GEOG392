#  Lab 7 - Garrett Dozier - GEOG 392 (GIS Programming) - Section 501
import arcpy

#Setting up workspace for variables below
arcpy.env.overwriteOutput = True 


# Here is the overall source
source = r"C:\Users\seths\Documents\Dozier\Lab7_dozier"



# Here are the RS composite bands (used RS imagery)
#Blue band
band1 = arcpy.sa.Raster(source + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF")
# Green band
band2 = arcpy.sa.Raster(source + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF")
# Red band
band3 = arcpy.sa.Raster(source + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF")
# NIR band
band4 = arcpy.sa.Raster(source + r"\LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF")
# compostie of all the bands (combining) - using the composite bands function
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\combination.tif")



# Hillshade (used DEM imagery)
# Azimuth 
azimuth = 315
#Altitude 
altitude = 45
# shadows or not?
shadows = "NO_SHADOWS"
# setting the z factor 
zfactor = 1
# creating a hillshade for the DEM - using the hillshade function
arcpy.ddd.HillShade(source + r"\n30_w097_1arc_v3.tif", source + r"\hillshade.tif", azimuth, altitude, shadows, zfactor)



# Calculating slope 
# output measurement 
output_measurement = "DEGREE"
# setting z factor 
zfactor2 = 1
# setting method, may need to not include this
method = "PLANAR"
# setting z_unit, may need to not include this
zunit = "METER"
arcpy.ddd.Slope(source + r"\n30_w097_1arc_v3.tif",source + r"\slope.tif", output_measurement, zfactor2, method, zunit)