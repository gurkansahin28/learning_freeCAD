"""
pytho3
author: Gurkan
2024/November/02, 15:11
"""
##############################################
### VECTOR ARITHMETIC IN FREECAD SCRIPTING ###
##############################################
### positioning, transforming and manipulating
#---------------------------------------------
# 1. importing freecad and the gui as aliases
import FreeCAD as App
import FreeCADGui as Gui

# 2. creating and naming a new document
docName = 'VectorArithmeticDoc'
doc = App.newDocument(docName)
doc.recompute()

# 3. making a box for the vector arithmetic attempts
print('adding a box to the document...')
width = 7
length = 5
height = 3
myBox = doc.addObject('Part::Box', 'MyBox')
myBox.Width = width
myBox.Length = length
myBox.Height = height
doc.recompute()
input('Press enter to continue!')
# 4. setting up the visualization
print('setting the visual presentation...')
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.activeDocument().activeView().viewTrimetric()
Gui.runCommand('Draft_ToggleGrid',1)
Gui.SendMsgToActiveView("ViewFit")
input('Press enter to continue!')

# 5. getting the existing object placement values
startingPlaBase = myBox.Placement.Base
print(startingPlaBase)
print(startingPlaBase.x)
print(startingPlaBase.y)
print(startingPlaBase.z)
doc.recompute()
input('Press enter to continue!')

print('setting parameters one by one...')
myBox.Placement.Base.x = -2
myBox.Placement.Base.y = 1
myBox.Placement.Base.z = -3
myBox.Placement.Base = startingPlaBase

# 6. Vector Arithmetic For the Base Feature
# 6.1. Addition
print('changing base of placement by adding...')
newPlaBase = App.Vector(3, 0, 0)
myBox.Placement.Base += newPlaBase
doc.recompute()
input('Press enter to continue!')

newerPlaBase = App.Vector(0, 3, 0)
resultVector = newPlaBase + newerPlaBase
print(resultVector)
myBox.Placement.Base = resultVector
doc.recompute()
input('Press enter to continue!')

# 6.2. Subtraction
print('changing base of placement by subtracting...')
existingPlaBase = myBox.Placement.Base
print(existingPlaBase)
newPlaBase = App.Vector(3, 3, 0)
resultVector = existingPlaBase - newPlaBase
myBox.Placement.Base = resultVector
doc.recompute()
input('Press enter to continue!')

# 6.3. Scaling
print('changing base of placement by scaling...')
myBox.Placement.Base = App.Vector(1, 1, 1)
existingPlaBase = myBox.Placement.Base
scalerVector = existingPlaBase * -2
print(scalerVector)
myBox.Placement.Base = scalerVector
doc.recompute()
input('Press enter to continue!')

# note: there are advanced topics like DOT and CROSS products