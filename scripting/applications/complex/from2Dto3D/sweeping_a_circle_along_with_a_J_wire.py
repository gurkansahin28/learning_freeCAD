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

### NAMING THE DOCUMENT ##########################
docName = 'Sweeping'
doc = App.newDocument(docName)

### SETTINGS AT THE BEGINNING #####################
pl = App.Placement()
pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)
 
# wire length
length = 20
 
# radius
r = 5

### MAKING A COMPLEX WIRE FOR SWEEPING #############
# vectors for the left side wire
lwVectors = []
lwVectors.append(App.Vector(0, 0, 0))
lwVectors.append(App.Vector(0, length, 0))

# left wire
lw = Draft.makeWire(lwVectors)
doc.recompute()
 
# the center of the left top arc according to Top view
clta = App.Vector(r, length, 0)
pl.Base = clta
start = 90.0
end = 180.0
 
# making the left top arc according to Top view
lta = Draft.make_circle(radius = r, placement = pl, face = False, startangle = start, endangle = end, support = None)
doc.recompute()

# joining the both wires
wireList = [lw, lta]
j = Draft.upgrade(wireList, delete = True)[0]
doc.recompute()

### MAKING THE SECTION AS A CIRCLE ###################
circle = Part.makeCircle(2)
sectObject = doc.addObject('Part::Feature', 'Section')

# rotating the section around the x axis 90 degree
circle.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(1, 0, 0), 90))
doc.recompute()

# linking the circle to Section as a Part::Feature
sectObject.Shape = circle
doc.recompute()

### SWEEPING #########################################
sweep = doc.addObject('Part::Sweep', 'Sweep')
sweep.Sections = [doc.Section]
sweep.Spine = doc.Wire
sweep.Solid = True
sweep.Frenet = False
doc.recompute()

### ADJUSTMENTS FOR VIEWING ###########################
Gui.SendMsgToActiveView("ViewFit")

 
