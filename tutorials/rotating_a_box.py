"""
pytho3
author: Gurkan
2024/November/02, 18:53
"""

################################################
### ROTATION OF A BOX IN FREECAD SCRIPTING #####
################################################
### 1. PREPARATIONS TO ROTATE A BOX ############
#---------------------------------------------
# 1.1. importing freecad and the gui as aliases
import FreeCAD as App
import FreeCADGui as Gui

# 1.2. creating and naming a new document
docName = 'RotatingBoxDoc'
doc = App.newDocument(docName)
doc.recompute()

# 1.3. making a box for the vector arithmetic attempts
width = 7
length = 5
height = 3
myBox = doc.addObject('Part::Box', 'MyBox')
myBox.Width = width
myBox.Length = length
myBox.Height = height
doc.recompute()
input('Press enter to continue!')

# 1.4. setting up the visualization
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.activeDocument().activeView().viewTrimetric()
Gui.runCommand('Draft_ToggleGrid',0)
Gui.SendMsgToActiveView("ViewFit")
input('Press enter to continue!')

### 2. ROTATIONS ###############################
#--- 2.1. SINGLE ROTATIONS ----------------------
# 2.1.1.rotating 15 degrees around X axis
deg = 15.0
aroundX = App.Vector(1, 0, 0)
rotationVector = App.Rotation(aroundX, deg)
myBox.Placement.Rotation = rotationVector
doc.recompute()
input('Press enter to continue!')

# rotating 0 degree for the starting position
deg = 0.0
aroundX = App.Vector(1, 0, 0)
rotationVector = App.Rotation(aroundX, deg)
myBox.Placement.Rotation = rotationVector
doc.recompute()
input('Press enter to continue!')
#--------------------------------------------------

# 2.1.2. rotating 30 degrees around Y axis
deg = 30.0
aroundY = App.Vector(0, 1, 0)
rotationVector = App.Rotation(aroundY, deg)
myBox.Placement.Rotation = rotationVector
doc.recompute()
input('Press enter to continue!')

# rotating 0.0 degree for the starting position
deg = 0.0
aroundY = App.Vector(0, 1, 0)
rotationVector = App.Rotation(aroundY, deg)
myBox.Placement.Rotation = rotationVector
doc.recompute()
input('Press enter to continue!')

# 2.1.3. rotating around Z axis
deg = 45.0
aroundZ = App.Vector(0, 0, 1)
rotationVector = App.Rotation(aroundZ, deg)
myBox.Placement.Rotation = rotationVector
doc.recompute()
input('Press enter to continue!')

# rotating 0.0 degree for the starting position
deg = 0.0
aroundZ = App.Vector(0, 0, 1)
rotationVector = App.Rotation(aroundZ, deg)
myBox.Placement.Rotation = rotationVector
doc.recompute()
input('Press enter to continue!')

#--- 2.2. COMBO ROTATIONS ---------------------
# attending values for rotating angles
degX = 15.0
degY = 15.0
degZ = 15.0

# 2.2.1. rotating in both axes of XY
rotationX = App.Rotation(aroundX, degX)
rotationY = App.Rotation(aroundY, degY)
rotationXYVector = rotationX.multiply(rotationY)
myBox.Placement.Rotation = rotationXYVector
doc.recompute()
input('Press enter to continue!')

# prestating to the beginning position
rotationX = App.Rotation(aroundX, degX-degX)
rotationY = App.Rotation(aroundY, degY-degY)
rotationXYVector = rotationX.multiply(rotationY)
myBox.Placement.Rotation = rotationXYVector
doc.recompute()
input('Press enter to continue!')

#--------------------------------------------
# 2.2.2. rotating in both axes of XZ
rotationX = App.Rotation(aroundX, degX)
rotationZ = App.Rotation(aroundZ, degZ)
rotationXYVector = rotationX.multiply(rotationZ)
myBox.Placement.Rotation = rotationXYVector
doc.recompute()
input('Press enter to continue!')

# prestating to the beginning position
rotationX = App.Rotation(aroundX, degX-degX)
rotationZ = App.Rotation(aroundZ, degZ-degZ)
rotationXZVector = rotationX.multiply(rotationZ)
myBox.Placement.Rotation = rotationXZVector
doc.recompute()
input('Press enter to continue!')

#---------------------------------------------
# 2.2.3. rotating in both axes of YZ
rotationY = App.Rotation(aroundY, degY)
rotationZ = App.Rotation(aroundZ, degZ)
rotationYZVector = rotationY.multiply(rotationZ)
myBox.Placement.Rotation = rotationYZVector
doc.recompute()
input('Lastly, press enter to continue!')

# prestating to the beginning position
rotationY = App.Rotation(aroundY, degY-degY)
rotationZ = App.Rotation(aroundZ, degZ-degZ)
rotationYZVector = rotationY.multiply(rotationZ)
myBox.Placement.Rotation = rotationYZVector
doc.recompute()

