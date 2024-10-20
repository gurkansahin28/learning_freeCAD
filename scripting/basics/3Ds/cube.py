import FreeCAD as App
import FreeCADGui as Gui

#################################################
docName = "ScriptingCube"
doc = App.newDocument(docName)
cube = doc.addObject("Part::Box", "MyCube")
cube.Length = 12
cube.Width = 12
cube.Height = 12
cube.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)