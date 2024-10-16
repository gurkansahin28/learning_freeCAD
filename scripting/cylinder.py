import FreeCAD as App
import FreeCADGui as Gui
docName = "ScriptingCylinder"
doc = App.newDocument(docName)
cylinder = doc.addObject("Part::Cylinder", "myCylinder")
cylinder.Radius = 5
cylinder.Height = 15
doc.recompute()

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
# App.closeDocument(docName)
