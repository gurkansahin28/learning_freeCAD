#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:48:37 2024

@author: gurkan
"""


import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Part
from FreeCAD import Base
 
###################################################
docName = 'Sweeping'
doc = App.newDocument(docName)
###################################################
pl = App.Placement()
pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)
 
# wire length
length = 20
 
# radius
r = 5
 
lwVectors = []
lwVectors.append(App.Vector(0, 0, 0))
lwVectors.append(App.Vector(0, length, 0))
#left wire
lw = Draft.makeWire(lwVectors)
doc.recompute()
 
# the center of the left top arc
clta = App.Vector(r, length, 0)
pl.Base = clta
start = 90.0
end = 180.0
 
# the left top arc
lta = Draft.make_circle(radius = r, placement = pl, face = False, startangle = start, endangle = end, support = None)
doc.recompute()

wireList = [lw, lta]
j = Draft.upgrade(wireList, delete = True)[0]
doc.recompute()
##################################################


circle = Part.makeCircle(2)
sectObject = doc.addObject('Part::Feature', 'Section')
###
circle.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1, 0, 0), 90))
doc.recompute()

sectObject.Shape = circle
doc.recompute()

sweep = doc.addObject('Part::Sweep', 'Sweep')
sweep.Sections = [doc.Section]
sweep.Spine = doc.Wire
sweep.Solid = True
sweep.Frenet = False
doc.recompute()

Gui.SendMsgToActiveView("ViewFit")

 
