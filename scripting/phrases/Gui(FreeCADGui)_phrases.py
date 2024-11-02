import FreeCADGui as Gui

Gui.SendMsjToActiveView('SaveAs')

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().viewTrimetric()
Gui.activeDocument().activeView().viewDimetric()
Gui.activeDocument().activeView().viewIsometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.Selection.clearSelection()
Gui.Selection.addSelection('Unnamed','Cylinder001')
Gui.ActiveDocument = Gui.getDocument(docName)
Gui.runCommand('Std_OrthographicCamera',0)
Gui.runCommand('Std_PerspectiveCamera',1)
Gui.runCommand('Draft_ToggleGrid',0)
Gui.activeDocument().activeView().setCameraType("Perspective")

myViewObject = Gui.ActiveDocument.getObject("ObjectName")
myGuiDocument = Gui.ActiveDocument
myView = Gui.ActiveDocument.ActiveView

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