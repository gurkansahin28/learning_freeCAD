#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:15:24 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
#################################################
docName = "MirroringASphere"
doc = App.newDocument(docName)
#####
radius = 5
sphere = doc.addObject("Part::Sphere", "MySphere")
sphere.Radius = radius

###
doc.recompute()

###
# Mirror the sphere across the XZ plane
mirror_matrix = App.Matrix()
mirror_matrix.scale(App.Vector(-1, 1, 1))  # Mirror across Y-axis (flip X)
mirrored_sphere = sphere.Shape.copy().transformGeometry(mirror_matrix)

# Add mirrored object to the document
mirrored_obj = doc.addObject("Part::Feature", "MirroredSphere")
mirrored_obj.Shape = mirrored_sphere

# Recompute to apply the mirror transformation
doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
