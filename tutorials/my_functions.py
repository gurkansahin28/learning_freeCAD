#----------------------------------------
def prepareGUI():
    GuiView = Gui.ActiveDocument.ActiveView
    GuiView.viewIsometric()
    GuiView.sendMessage('ViewFit')
    GuiView.setAxisCross(True)
    Gui.runCommand('Draft_ToggleGrid',0)
    Gui.runCommand('Draft_ToggleGrid',0)
    doc.recompute()
#----------------------------------------
def closeDoc():
    App.closeDocument(App.ActiveDocument.Name)
#----------------------------------------
def getObjPlaMatrix(Obj):
    # Selecting the object
    selObj = App.ActiveDocument.getObject(Obj)
    
    # object placement matrix
    opm = selObj.Placement.toMatrix()
    
    # object placement matrix positions
    opm_pos = (opm.A14, opm.A24, opm.A34)
    
    return opm_pos
#----------------------------------------

#----------------------------------------
