#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:33:57 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Draft
#################################################
docName = "MakingDetailedRectangle"
doc = App.newDocument(docName)
#####
simpleRectOne = Draft.make_rectangle(4000, 1000)
simpleRectTwo = Draft.make_rectangle(1000, 4000)
####
zVector = App.Vector(0, 0, 1)
pVector = App.Vector(1000, 1000, 0)
newPlacement = App.Placement(pVector, App.Rotation(zVector, 45))
detailedRect = Draft.make_rectangle(3500, 250, placement = newPlacement)
doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
