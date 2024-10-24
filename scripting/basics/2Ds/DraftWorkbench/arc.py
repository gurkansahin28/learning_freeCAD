import FreeCAD as App
import FreeCADGui as Gui
import Draft
#################################################
docName = "DraftArc"
doc = App.newDocument(docName)

pl = FreeCAD.Placement()
pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)
pl.Base = FreeCAD.Vector(0.0, 0.0, 0.0)
start = 90.0
end = 180.0

r = 5.0
arc = Draft.make_circle(radius = r, placement=pl, face=False, startangle=start, endangle=end, support=None)
doc.recompute()

##################################################
Gui.SendMsgToActiveView('ViewFit')
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#Gui.activeDocument().activeView().viewIsometric()
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)

