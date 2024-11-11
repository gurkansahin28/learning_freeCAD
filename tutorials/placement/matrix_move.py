#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:01:10 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui

### Creating a document with given name
docName = 'MatricesDoc'
doc = App.newDocument(docName)

### Creating a box object
box = doc.addObject('Part::Box', 'MyBox')
box.Length = 20
box.Height = 10
box.Width = 30
doc.recompute()

input('Press Enter to continue!.. ')

### Adjusting Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
GuiView.viewIsometric()
GuiView.fitAll()
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
doc.recompute()

input('Press Enter to continue!.. ')

### Selecting the box
selectedObj = doc.getObject('MyBox')
selectedObjPla = selectedObj.Placement
selectedObjPlaMat = selectedObjPla.toMatrix()


### Picking out the existing placement parameters
startingX = selectedObjPlaMat.A14
startingY = selectedObjPlaMat.A24
startingZ = selectedObjPlaMat.A34

### Preparing the position with factor variable
factor = 3
newX = startingX + factor
newY = startingY + factor
newZ = startingZ + factor

### Moving the box to new placement
selectedObjPlaMat.move(newX, newY, newZ)
selectedObj.Placement = selectedObjPlaMat
doc.recompute()

input('Press Enter to move back!.. ')

### Resetting the box to its original placement
selectedObjPlaMat.A14 = startingX
selectedObjPlaMat.A24 = startingY
selectedObjPlaMat.A34 = startingZ
selectedObj.Placement = App.Placement(App.Vector(startingX, startingY, startingZ), App.Rotation())
doc.recompute()
