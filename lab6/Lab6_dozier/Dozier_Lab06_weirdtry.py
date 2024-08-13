#  Lab 6 - Garrett Dozier - GEOG 392 (GIS Programming) - Section 501
import arcpy, sys

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

        
        Campusgdb = r"C:\Users\seths\Documents\Dozier\Lab4\Campus.gdb"
        inputLayer = Campusgdb + r"\GarageParking"
        

        #Creating the object for the actual project 

        project = arcpy.mp.ArcGISProject(r"C:\Users\seths\Documents\ArcGIS\Projects\Lab6_Dozier_GEOG392\Lab6_Dozier_GEOG392.aprx")

        # Creating and Testing the map object from above
        maps = project.listMaps()[0]
        print(maps.name)

        layers = map.listLayers()

        for layer in layers:
            if layer.isFeatureLayer == True:
                if layer.name.lower() == inputLayer.lower:
                    symbology = layer.symbology 
                    if hasattr(symbology, "renderer") == True:
                        symbology.updateRenderer("GraduatedColorsRenderer")
                        symbology.renderer.breakCount = 5
                        symbology.renderer.colorRamp = project.listColorRamps('Blues (continuous')[0]
                        layer.symbology = symbology

        project.saveACopy(r"C:\Users\seths\Documents\ArcGIS\Projects\Lab6_Dozier_GEOG392\Lab6_Dozier_GEOG392.aprx")
                                        
    