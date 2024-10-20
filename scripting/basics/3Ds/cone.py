#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:29:34 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Part
#################################################
docName = 'MakingCone'
doc = App.newDocument(docName)

#####
cone = doc.addObject('Part::Cone', 'MyCone')
cone.Radius1 = 5
cone.Radius2 = 0
cone.Height = 10

##################################################
Gui.SendMsgToActiveView('ViewFit')
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
