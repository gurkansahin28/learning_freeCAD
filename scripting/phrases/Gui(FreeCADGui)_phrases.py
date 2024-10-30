import FreeCADGui as Gui

Gui.SendMsjToActiveView('SaveAs')

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)