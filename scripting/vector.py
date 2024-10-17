import FreeCAD as App
import FreeCADGui as Gui

docName = "TestingVectors"
width = 25
length = 15
height = 45
doc = App.newDocument(docName)
box = doc.addObject("Part::Box", "MyBox")

box.Width = width
box.Length = length
box.Height = height
doc.recompute()

myVec = App.Vector(2, 0, 0)
box.Placement.Base = myVec

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
#App.closeDocument(docName)
