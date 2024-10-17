import FreeCAD as App
import FreeCADGui as Gui

docName = "RotateTheObject"
doc = App.newDocument(docName)
box = doc.addObject("Part::Box", "MyBox")

box.Length = 10
box.Width = 5
box.Height = 25

box.Placement.Rotation = App.Rotation(App.Vector(0, 0, 1), 45)
doc.recompute()

Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
#App.closeDocument(docName)
