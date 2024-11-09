#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:19:30 2024

@author: gurkan
"""
##############################################
### COLORIZING IN FREECAD SCRIPTING ##########
##############################################

# importing freecad and the gui as aliases
import FreeCAD as App
import FreeCADGui as Gui
import random

# creating and naming a new document
docName = 'ColourisingDoc'
doc = App.newDocument(docName)
doc.recompute()

# adding a box to the document
box = doc.addObject("Part::Box", "ColoredBox")
box.Placement.Base = App.Vector(1, 1, 0)
doc.recompute()

# setting up the visualization
Gui.activeDocument().activeView().viewAxometric()
Gui.runCommand('Draft_ToggleGrid', 0)
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.SendMsgToActiveView('ViewFit')
doc.recompute()

howManyTimes = 15

while howManyTimes > 0:
    input('Press the Enter key to continue!')
    howManyTimes -= 1
    box = doc.getObject('ColoredBox')
    rRed = random.random()
    rGreen = random.random()
    rBlue = random.random()
    rTrans= random.randint(50, 100)
    print(f'{rRed} {rGreen} {rBlue}')
    box.ViewObject.ShapeColor = (rRed, rGreen, rBlue)
    box.ViewObject.Transparency = rTrans
    doc.recompute()
    
