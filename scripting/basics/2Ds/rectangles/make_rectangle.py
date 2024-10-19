import FreeCAD as App
import FreeCADGui as Gui
import Draft

################################################
docName = "MakeRectangle"
doc = App.newDocument(apName)

length = 50
width = 30
rect = Draft.makeRectangle(length, width)
doc.recompute()

#################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
