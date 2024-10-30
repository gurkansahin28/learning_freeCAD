import FreeCADGui as Gui

Gui.SendMsjToActiveView('ViewFit')

Gui.activeDocument().activeView().viewAxometric()