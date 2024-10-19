#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:28:16 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
#################################################
docName = "CopyAndTranslateTheCube"
doc = App.newDocument(docName)

#####
length = width = height = 10
cube = doc.addObject("Part::Box", "MyCube")
cube.Length = cube.Width = cube.Height = 10

###
doc.recompute()

###
copy_cube = cube.Shape.copy()
translated_copy = copy_cube.copy().translate(App.Vector(15, 0, 0))

###
copy_object = doc.addObject("Part::Feature", "TranslatedCube")
copy_object.Shape = translated_copy

###
doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)