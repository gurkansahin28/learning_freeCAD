import FreeCAD as App
import FreeCADGui as Gui

docName = "TranslateAndRotateTheObject"
doc = App.newDocument(docName)
box = doc.addObject("Part::Box", "MyBox")

box.Length = 10
box.Width = 5
box.Height = 25

x = 20
y = 10
z = 5

box.Placement.Base = App.Vector(x, y, z)
box.Placement.Rotation = App.Rotation(App.Vector(x, y, z), 45)

Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
#App.closeDocument(docName)
