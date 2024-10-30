
import FreeCAD as App
import FreeCADGui as Gui
import PartDesignGui
from BOPTools import BOPFeatures

#------------------------------------
docName = 'BooleanOperationToolsDoc'
doc = App.newDocument(docName)
#------------------------------------
#bp.make_cut()
#bp.make_common()
#bp.make_fuse()
#bp.make_section()

bp = BOPFeatures.BOPFeatures(App.activeDocument())
bp.make_cut(["MyBox", "MyCylinder", ])
App.ActiveDocument.recompute()
#-----------------------------------------
doc = App.getDocument("Unnamed")
obj = doc.getObject("Cylinder001")
shp = obj.Shape
#------------------------------------------
obj.Placement.Base = App.Vector(15,20,0)
obj.Placement.Rotation = App.Rotation(App.Vector(15,20,0), 45)
#-------------------------------------------
