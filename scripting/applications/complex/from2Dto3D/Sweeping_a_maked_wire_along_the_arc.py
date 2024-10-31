#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 00:05:46 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Draft

# setting up document name
docName = 'SweepingDoc'
doc = App.newDocument
doc = App.newDocument(docName)

# section vectors
sV1 = App.Vector(0, 0, 0)
sV2 = App.Vector(0, 5, 0)
sV3 = App.Vector(8, 5, 0)
sV4 = App.Vector(8, 0, 0)
sV5 = App.Vector(6, 0, 0)
sV6 = App.Vector(6, 3, 0)
sV7 = App.Vector(2, 3, 0)
sV8 = App.Vector(2, 0, 0)
Vectors = [sV1, sV2, sV3, sV4, sV5, sV6, sV7, sV8]
sectionWire = Draft.make_wire(Vectors, closed = True)
sectionWire.Label = 'Section'
doc.recompute()

# making an arc of 90 degree through the circle method
spineArc = Draft.make_circle(20, startangle = 90, endangle = 180)
spineArc.Label = 'SpineArc'
spineArc.Placement = App.Placement(App.Vector(20, 0, 0), App.Rotation(App.Vector(1, 0, 0), 90))
doc.recompute()

# sweeping sectionWire along the spineWire
sweep = doc.addObject('Part::Sweep', 'Sweeping')
sweep.Sections = doc.getObjectsByLabel('Section')
#sweep.Spine = doc.getObject('Arc')
sweep.Spine = doc.getObjectsByLabel('SpineArc')[0]
sweep.Solid = True
sweep.Frenet = False
doc.recompute()

# Gui adjustments for visual presentation
Gui.activeDocument().activeView().viewTrimetric()
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.SendMsgToActiveView('ViewFit')
