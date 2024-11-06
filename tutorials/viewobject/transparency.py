#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:45:51 2024

@author: gurkan
"""

##############################################
### TRANSPARENCY IN FREECAD SCRIPTING ########
##############################################

# importing freecad and the gui as aliases
import FreeCAD as App
import FreeCADGui as Gui

# creating and naming a new document
docName = 'TransparencyDoc'
doc = App.newDocument(docName)
doc.recompute()

# adding a box to the document
box = doc.addObject("Part::Box", "ColoredBox")
red, green, blue = 255, 0, 0
box.ViewObject.ShapeColor = (red, green, blue)
box.ViewObject.Transparency = 100
doc.recompute()

# setting up the visualization
Gui.activeDocument().activeView().viewAxometric()
Gui.runCommand('Draft_ToggleGrid', 0)
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.SendMsgToActiveView('ViewFit')

# increasing the opacity of the box
transparency = box.ViewObject.Transparency
while transparency > 0:
    input('Press the Enter key to continue!')
    transparency -= 10
    box.ViewObject.Transparency = transparency

doc.recompute()
