import FreeCAD as App
import FreeCADGui as Gui

docName = "TranslateAnObject"
doc = App.newDocument(docName)

box = doc.addObject("Part::Box", "MyBox")

box.Length = 10
box.Width = 15
box.Height = 20

box.Placement.Base = App.Vector(20, 10, 5)

doc.recompute()

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
#App.closeDocument(docName)

