import FreeCAD as App
import FreeCADGui as Gui
import Part
###############################################
docName = "MakingBox"
doc = App.newDocument(docName)
###
myPart = doc.addObject("Part::Box", "myBox")
###
x = y = z = 2
cube = Part.makeBox(x, y, z)
myPart.Shape = cube
doc.recompute()
###
### adjustments for the pose of activeView ###################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
# App.closeDocument(docName)
