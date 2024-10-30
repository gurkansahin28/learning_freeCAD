import FreeCADGui as Gui

Gui.SendMsjToActiveView('ViewFit')

Gui.SendMsjToActiveView('SaveAs')

Gui.activeDocument().activeView().viewAxometric()