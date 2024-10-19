import FreeCAD as App
import FreeCADGui as Gui
import Part
#################################################
docName = "UnionCubeAndSphere"
doc = App.newDocument(docName)

#####
length = width = height = 20
cube = doc.addObject("Part::Box", "MyCube")
cube.Length = length
cube.Width = width
cube.Height = height

###
sphere = doc.addObject("Part::Sphere", "MySphere")
sphere.Radius = 10

###
sphere.Placement.Base = App.Vector(15, 15, 10)

doc.recompute()

fusion = doc.addObject("Part::Fuse", "CubeSphereFusion")
fusion.Base = cube
fusion.Tool = sphere

doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
