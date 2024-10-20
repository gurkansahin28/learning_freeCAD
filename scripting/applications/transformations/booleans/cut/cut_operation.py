#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:23:12 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part

#################################################
docName = "CutOperation"
doc = App.newDocument(docName)
#####
length = width = heigth = 20
cube = doc.addObject("Part::Box", "MyCube")
cube.Length = length
cube.Width = width
cube.Height = heigth

###
radius = 10
sphere = doc.addObject("Part::Sphere", "MySphere")
sphere.Radius = radius

###
sphere.Placement.Base = App.Vector(15, 15, 10)

###
doc.recompute()

###
cut = doc.addObject("Part::Cut", "SphericHollow")
cut.Base = cube
cut.Tool = sphere

###
doc.recompute()

###
cut.Placement.Base = App.Vector(20, 10, 5)

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
