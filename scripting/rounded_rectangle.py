import FreeCAD as App
import FreeCADGui as Gui
import Draft

docName = "RoundedRectangleDoc"
doc = App.newDocument(docName)

length = 30
width = 20

# Create the rectangle at the origin
rect = Draft.makeRectangle(length, width)

fillet_radius = 5
rect.FilletRadius = fillet_radius

doc.recompute()

Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
#App.closeDocument(docName)
