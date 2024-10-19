import FreeCAD as App
import FreeCADGui as Gui
import Part

docName = "ChamferingTheBox"
doc = App.newDocument(docName)

cube = doc.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)

chmfr = doc.addObject("Part::Chamfer", "myChamfer")
chmfr.Base = doc.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
Gui.ActiveDocument.myCube.Visibility = False
doc.recompute()

### adjustments for the pose of activeView ###################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
# App.closeDocument(docName)
