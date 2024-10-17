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

#------------------------------------
# New (Ctrl + N)
# Create a new empty document
App.newDocument()
#------------------------------------
from BOPTools import BOPFeatures
bp = BOPFeatures.BOPFeatures(App.activeDocument())
bp.make_cut(["MyBox", "Cylinder", ])
App.ActiveDocument.recompute()
#-----------------------------------------
