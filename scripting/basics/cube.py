import FreeCAD as App
import FreeCADGui as Gui
doc = App.newDocument("ScriptingCube")
cube = doc.addObject("Part::Box", "MyCube")
cube.Length = 12
cube.Width = 12
cube.Height = 12
cube.recompute()

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()

# App.closeDocument("TestDocument")
