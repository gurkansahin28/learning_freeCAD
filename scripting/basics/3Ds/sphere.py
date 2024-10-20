#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:16:55 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
#################################################
docName = 'MakingSphere'
doc = App.newDocument(docName)

#####
sphere = doc.addObject('Part::Sphere', 'MySphere')
sphere.Radius = 10

doc.recompute()

##################################################
Gui.SendMsgToActiveView('ViewFit')
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)