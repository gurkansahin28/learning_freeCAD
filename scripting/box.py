#################################################################
import FreeCAD as App
import FreeCADGui as Gui
docName = "TestingScripting"
width = 25
length = 15
height = 45
doc = App.newDocument(docName)
box = doc.addObject("Part::Box", "MyBox")
box.Width = width
box.Length = length
box.Height = height
doc.recompute()
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
###################################################################
