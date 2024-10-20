#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:55:19 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
#from BOPTools import BOFeatures

# creating a new document
docName = "IntersectingForms"
doc = App.newDocument(docName)

# creating and adjusting a box
length = width = height = 10
myBox = doc.addObject("Part::Box","Box")
myBox.Label = "Cube"
myBox.Length = length
myBox.Width = width
myBox.Height = height

doc.recompute()

# creating and adjusting a cone
radius1 = 0
radius2 = 4
myCone = doc.addObject("Part::Cone", "Cone")
myCone.Label = "Cone"
myCone.Radius1 = radius1
myCone.Radius2 = radius2
myCone.Height = height

doc.recompute()

# creating an intersection and bounding forms
bp = BOPFeatures.BOPFeatures(doc)
bp.make_multi_common(["Box", "Cone",])

doc.recompute()

### adjustments for the pose of activeView ###################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)

#doc.saveAs("/absolute/path/to/your/file.FCStd")

# App.closeDocument(docName)
