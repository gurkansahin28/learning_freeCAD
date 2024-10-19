#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:05:32 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
#################################################
docName = "ShearingABox"
doc = App.newDocument(docName)
#####
length = width = height = 10
cube = doc.addObject("Part::Box", "MyCube")
cube.Length = length
cube.Width = width
cube.Height = height

###
doc.recompute()

###
shear_matrix = App.Matrix()
shear_matrix.A11 = 1
shear_matrix.A12 = 0.5
shear_matrix.A13 = 0

sheared_cube = cube.Shape.copy().transformGeometry(shear_matrix)
sheared_obj = doc.addObject("Part::Feature", "ShearedCube")
sheared_obj.Shape = sheared_cube

###
doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)