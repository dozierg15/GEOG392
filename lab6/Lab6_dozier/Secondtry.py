#  Lab 6 - Garrett Dozier - GEOG 392 (GIS Programming) - Section 501
import arcpy

#Setting up workspace for variables below
arcpy.env.overwriteOutput = True 



class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "RenderingToolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [ArcRenderer]



class ArcRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "ArcRenderer"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
        displayName="Input Project File",
        name= "inputProoject",
        datatype="DEFile",
        parameterType="Required",
        direction="Input")
        param1 = arcpy.Parameter(
        displayName="Input Layer Name",
        name="inputLayer",
        datatype="GPString", 
        parameterType="Required",
        direction="Input")   
        param2 = arcpy.Parameter(
        displayName="Output Project File",
        name="outputProject",
        datatype="DEFile",
        parameterType="Required",
        direction="Output")    
        params = [param0,param1,param2]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
# Reference to our .aprx
project = arcpy.mp.ArcGISProject(r"C:\Users\seths\Documents\Dozier\Lab6" + r"\\Lab6_Dozier.aprx")
# Grab the first map in the .aprx
campus = project.listMaps('Map')[0]
# Loop through available layers in the map
for layer in campus.listLayers():
    # Check if layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Check if it has a 'renderer' attribute
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is 'GarageParking'
            if layer.name == "GarageParking":
                # Update the copy's renderer to be 'GraduatedColorsRenderer'
                symbology.updateRenderer('GraduatedColorsRenderer')
                # Tell arcpy which field we want to base our choropleth off of
                symbology.renderer.classificationField = "Shape_Area"
                # Set how many classes we'll have 
                symbology.renderer.breakCount = 5
                # Set the color ramp
                symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("NOT GarageParking")
project.saveACopy(r"C:\Users\seths\Documents\Dozier\Lab6" + r"\\Lab6_Dozier.aprx")