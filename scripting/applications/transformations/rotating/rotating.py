#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:49:44 2024

@author: gurkan
"""
# aliases for convenient coding
import FreeCAD as App
import FreeCADGui as Gui

# creating a new document given a name
docName = "RotatingObjectDoc"
doc = App.newDocument(docName)
doc.recompute()

# creating a cube instance
width = length = height = 10
cube = doc.addObject('Part::Box', 'myCube')

# giving values required 
cube.Length = length
cube.Width = width
cube.Height = height

# setting up the placement of the cube
cube.Placement.Base = App.Vector(5, 5, 0)

# rotating the cube 20 degree around the Z axis
cube.Placement.Rotation = App.Rotation(App.Vector(0, 0, 1), 20)
doc.recompute()

##################################################
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.SendMsgToActiveView('ViewFit')
###################################################

#App.closeDocument(docName)
