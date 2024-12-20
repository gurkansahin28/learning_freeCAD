"""
INTRO
-----
This document was prepared for educational purposes
for whom are interested in design, STEAM and Art.

The code document aims to display 
how to operate some applications in FreeCAD Scripting 
as below mentioned.

AIMS
----
    1. To use Vectors
    2. To creat line segments
    3. To creat a geometry for a Draft shape
    4. To apply Revolution to the shape to obtain a solid form
    5. To apply Fillet feature to the revolved solid
    6. To set up visualization 

CONTENTS
--------
    A. IMPORTS
        1. Importing required libraries as aliases
        2. Importing Part to use its LineSegment methode

    B. SPECIFIC FUNCTIONS
        1. The function for the presentation
        2. The function to inform user
        3. The function to get the plane for the sketch

    C. DOCUMENT
        1. Creating a FreeCAD document with given name
            a. a name for the document
            b. creating the document

    D. BODY
        1. Creating Body object with given parameters
            a. parameters
            b. creation of the body

    E. SKETCH
        1. Creation a Sketch via given parameters
            a. parameters
            b. creating the skectch


        2. Set the plane for the sketch (XY Plane)
            a. Attach the sketch to the XY plane using its attachment system
                1. attaching

        3. From Vectors to the Sketch
            a. Defining Edge Vectors for lines
            b. Creating line segments from vectors
            c. Generating rectangle form line segments geometry

    F. REVOLUTION
        1. Creating Revolution through the parameters and settings
            a. parameters
            b. settings


    G. FILLET OPERATION
        1. Fillet operation by the parameters and settings
            a. parameters
            b. settings


Created on Mon Nov 25 16:18:00 2024

FreeCAD Version: 1.0.0

license: CCO 1.0
https://creativecommons.org/publicdomain/zero/1.0/

@author: gurkan
gurkansahin28@gmail.com
"""

### A. IMPORTS
## 1. Importing required libraries as aliases
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
# 2. Importing Part to use its LineSegment methode
import Part # type: ignore

### B. SPECIFIC FUNCTIONS
## 1. The function for the presentation
def setVisuality():
    # Setting up visualization
    GuiView = Gui.ActiveDocument.ActiveView
    # Setting the scene isometric view
    GuiView.viewIsometric()
    # Displaying crossing axes
    GuiView.setAxisCross(True)
    # Fitting the scene in the frame
    GuiView.fitAll()
    pass

## 2. The function to inform user
def txtRv(msg):
    FreeCAD.Console.PrintMessage(f'\n{msg}') # type: ignore
    pass

## 3. The function to get the plane for the sketch
def getPlane(body, role="XY_Plane"):
    # handling the body object collection
    bodyObjects = body.Document.Objects
    # investigating whether the object has 'Role' attribute
    hasObjAttr = hasattr(obj, 'Role')
    # getting informed what the object role is
    is_role = (obj.Role == role)
    # creating a container variable to get the parent info
    objGroupName = obj.getParentGeoFeatureGroup()
    # testifying the name whether it is 'body'
    is_groupName_body = (objGroupName == body)
    # defining a list to contain conditional planes
    planes = [obj for obj in bodyObjects if hasObjAttr and is_role and is_groupName_body]
    # if it has a only one member return it
    if len(planes) == 1:
        return planes[0]
    # else raise an error message on the Report view and quit
    else:
        errMsg = f"Error: Unable to find origin object with role = {role} for {body.Label}\n"
        App.Console.PrintError(errMsg)
        return None


input('Press Enter to create a new document!..')
### C. DOCUMENT
## 1. Creating a FreeCAD document with given name
# a. a name for the document
docName = 'RevoFilletDoc'
# b. creating the document
doc = App.newDocument(docName)
doc.recompute()
txtRv('The document has been created.')

input('Press Enter to create a Body object!..')
### D. BODY
## 1. Creating Body object with given parameters
# a. parameters
objName = 'MyBody'
objFromLib = 'PartDesign::Body'
# b. creation of the body
body = doc.addObject(objFromLib, objName)
txtRv('The Body object created!..')

input('Press Enter for the Sketch object!..')
### E. SKETCH
## 1. Creation a Sketch via given parameters
# a. parameters
objName = 'MyRect'
objFromLib = 'Sketcher::SketchObject'
# b. creating the skectch
sketch = body.newObject(objFromLib, objName)
doc.recompute()
txtRv('The Skecth object has been created!..')

input('Press Enter to create a Rectangle!..')
## 2. Set the plane for the sketch (XY Plane)
# a. Attach the sketch to the XY plane using its attachment system
# 1. attaching
xyplane = getPlane(body, 'XY_Plane')
sketch.AttachmentSupport = xyplane
sketch.MapMode = 'FlatFace'
doc.recompute()

## 3. From Vectors to the Sketch
# a. Defining Edge Vectors for lines
topEdgeV1 = App.Vector(10, 8, 0)
topEdgeV2 = App.Vector(20, 8, 0)
rightEdgeV1 = App.Vector(20, 8, 0)
rightEdgeV2 = App.Vector(20, 0, 0)
bottomEdgeV1 = App.Vector(20, 0, 0)
bottomEdgeV2 = App.Vector(10, 0, 0)
leftEdgeV1 = App.Vector(10, 0, 0)
leftEdgeV2 = App.Vector(10, 8, 0)

# b. Creating line segments from vectors
topEdge = Part.LineSegment(topEdgeV1, topEdgeV2)
rightEdge = Part.LineSegment(rightEdgeV1, rightEdgeV2)
bottomEdge = Part.LineSegment(bottomEdgeV1, bottomEdgeV2)
leftEdge = Part.LineSegment(leftEdgeV1, leftEdgeV2)

# c. Generating rectangle form line segments geometry
rect = [
    sketch.addGeometry(topEdge),
    sketch.addGeometry(rightEdge),
    sketch.addGeometry(bottomEdge),
    sketch.addGeometry(leftEdge)
]
doc.recompute()
txtRv('The Rectangle has been created!..')
setVisuality()

input('Press Enter to start Revolution operation!..')
### F. REVOLUTION
## 1. Creating Revolution through the parameters and settings
# a. parameters
objName = 'MyRevo'
objFromLib = 'PartDesign::Revolution'
obj = body.newObject(objFromLib, objName)
revoAxis = ['V_Axis']
# b. settings
obj.Profile = sketch
obj.ReferenceAxis = (sketch, revoAxis)
obj.Angle = 270.0
obj.Reversed = True
sketch.Visibility = False
doc.recompute()
txtRv('The Revolution object has been created!..')
setVisuality()

input('Press to make Fillet operation!..')
### G. FILLET OPERATION
## 1. Fillet operation by the parameters and settings
# a. parameters
doc = App.getDocument(docName)
body = doc.getObject('MyBody')
revoObj = body.getObject('MyRevo')
objName = 'MyFillet'
objFromLib = 'PartDesign::Fillet'
obj = body.newObject(objFromLib, objName)
# b. settings
obj.Base = (revoObj, [f"Edge{i}" for i in revoObj.Shape.Edges])
obj.Radius = 1.0
obj.UseAllEdges = True
revoObj.Visibility = False
doc.recompute()
txtRv('The Rovolution has been done!..')

setVisuality()
txtRv('Visulization improved!..')

