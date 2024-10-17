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
