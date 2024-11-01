#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:47:59 2024

@author: gurkan
"""
# importing for aliases to get conveniences
import FreeCAD as App
import FreeCADGui as Gui

# giving a suitable name to the document
docName = 'PlacementJobsDoc'
doc = App.newDocument(docName)
doc.recompute()

# adding a box from Part::Box
box = doc.addObject('Part::Box', 'mybox')
box.Length = 20
box.Height = 10
box.Width = 30
doc.recompute()

# setting up Gui before replacement works
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView('ViewFit')

#--- ROTATION --------------------------------
# setting the rotation parameters
aroundX = App.Vector(1, 0, 0)
aroundY = App.Vector(0, 1, 0)
aroundZ = App.Vector(0, 0, 1)
degrees = 30

# rotating only
box.Placement.Rotation = App.Rotation(aroundX, degrees)
doc.recompute()

#--- TRANSLATION ------------------------------
# setting the all translation parameters
box.Placement.Base = App.Vector(10, 0, 0)
box.Placement.Base = App.Vector(5, 10, 0)
doc.recompute()

# setting axis per axis
box.Placement.Base.z = 10

box.Placement.Base.x = 0
box.Placement.Base.z = 0
box.Placement.Base.y = 0
doc.recompute()

#--- ADDING INCREMENTAL CHANGES -----------------
# obtaining existing position
placement = box.Placement
incrementalFactor = App.Vector(-6, 0, 0)
placement.Base += incrementalFactor
box.Placement = placement
doc.recompute()

#--- SETTING THE WHOLE PLACEMENT PARAMETERS -----
base = App.Vector(-3, -1, -5)
aroundY = App.Vector(0, 1, 0)
degrees = 60
rotation = App.Rotation(aroundY, degrees)
box.Placement = App.Placement(base, rotation)
doc.recompute()


