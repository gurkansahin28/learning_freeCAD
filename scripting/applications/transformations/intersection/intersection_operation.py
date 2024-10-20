#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:39:30 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Part
#################################################
docName = "IntersectionOperation"
doc = App.newDocument(docName)
#####
length = width = height = 20
cube = doc.addObject("Part::Box", "MyCube")
cube.Length = length
cube.Width = width
cube.Height = height

###
radius = 10
sphere = doc.addObject("Part::Sphere", "MySphere")
sphere.Radius = radius

###
x = y = 15
z = 10
sphere.Placement.Base = App.Vector(x, y, z)

###
doc.recompute()

###
intersection = doc.addObject("Part::Common", "IntersectionOfCubeAndSphere")
intersection.Base = cube
intersection.Tool = sphere

###
doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)