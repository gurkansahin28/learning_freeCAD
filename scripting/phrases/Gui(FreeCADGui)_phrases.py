import FreeCADGui as Gui

Gui.SendMsjToActiveView('SaveAs')

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.Selection.clearSelection()
Gui.Selection.addSelection('Unnamed','Cylinder001')

# WORKBENCHES
########################################
Gui.activateWorkbench("PartWorkbench")
########################################
Gui.activateWorkbench("PartDesignWorkbench")
########################################
Gui.activateWorkbench("SketcherWorkbench")
#########################################
Gui.activateWorkbench("OpenSCADWorkbench")
##########################################

##########################################