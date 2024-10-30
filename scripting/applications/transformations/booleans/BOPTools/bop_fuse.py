#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:59:38 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
from BOPTools import BOPFeatures

#------------------------------------
docName = 'BooleanOperationToolsCut'
doc = App.newDocument(docName)
#------------------------------------
myBox = doc.addObject('Part::Box', 'MyBox')
myBox.Height = 7
myBox.Width = 7
myBox.Length = 7
doc.recompute()

myCylinder = doc.addObject('Part::Cylinder', 'MyCylinder')
myCylinder.Radius = 5
myCylinder.Angle = 30
myCylinder.Height = 9
doc.recompute()

bop = BOPFeatures.BOPFeatures(doc)
bop.make_fuse(['MyBox', 'MyCylinder', ])
doc.recompute()

Gui.runCommand('Std_PerspectiveCamera',1)
Gui.SendMsgToActiveView("ViewFit")
