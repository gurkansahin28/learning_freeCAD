# WORKBENCHES
########################################
Gui.activateWorkbench("PartWorkbench")
########################################
Gui.activateWorkbench("PartDesignWorkbench")
########################################
Gui.activateWorkbench("SketcherWorkbench")
import PartDesignGui
#########################################
Gui.activateWorkbench("OpenSCADWorkbench")
##########################################
Gui.Selection.clearSelection()
Gui.Selection.addSelection('Unnamed','Cylinder001')
##########################################
#------------------------------------
# New (Ctrl + N)
# Create a new empty document
App.newDocument()
#------------------------------------
#bp.make_cut()
#bp.make_common()
#bp.make_fuse()
#bp.make_section()
from BOPTools import BOPFeatures
bp = BOPFeatures.BOPFeatures(App.activeDocument())
bp.make_cut(["MyBox", "Cylinder", ])
App.ActiveDocument.recompute()
#-----------------------------------------
doc = App.getDocument("Unnamed")
obj = doc.getObject("Cylinder001")
shp = obj.Shape
#------------------------------------------
obj.Placement.Base = App.Vector(15,20,0)
obj.Placement.Rotation = App.Rotation(App.Vector(15,20,0), 45)
#-------------------------------------------
