#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:02:32 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui

import Draft
#import math
####################################################
docName = 'Roteted'

doc = App.newDocument(docName)

pl = FreeCAD.Placement()
pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)
pl.Base = FreeCAD.Vector(0.0, 0.0, 0.0)
l = 10.0
h = 10.0
rec = Draft.make_rectangle(length=l, height=h, placement=pl, face=False, support=None)

Draft.autogroup(rec)
doc.recompute()

##################################################
Gui.SendMsgToActiveView('ViewFit')
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#Gui.activeDocument().activeView().viewIsometric()
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
