import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Part
#################################################
docName = ""
doc = App.newDocument(docName)
#####


##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
