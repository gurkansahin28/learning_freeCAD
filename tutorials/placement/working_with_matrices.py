#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This document is about the Matrix class in FreeCAD scripting.
It aims to operate three features of it as translating, rotating and scaling.

Index of the Document
---------------------
    A. Preparations
        1. Importing FreeCAD and its Gui as aliases for convenience coding
        2. Creating a FreeCAD document given a suitable name
        3. Creating a box to work on
        4. Preparing the Gui for visualizing
        5. Selecting the box previously created
        6. Obtaining the existing box placement values as Matrix
        7. Preparing the position parameters with factor variable
    B. Matrix Transformations
        1. Translating
        2. Rotating
        3. Scaling
    C. Hiding and Showing Objects

Created on Mon Nov 11 17:01:10 2024

@author: gurkan
"""

### A. PREPARATIONS #######################
## A.1. Importing FreeCAD and its Gui as aliases for convenience coding
import FreeCAD as App
import FreeCADGui as Gui
import random

## A.2. Creating a FreeCAD document given a suitable name
docName = 'MatricesDoc'
doc = App.newDocument(docName)

input('Press Enter to create a Box!.. ')

## A.3. Creating a box to work on
box = doc.addObject('Part::Box', 'MyBox')
box.Length = 20
box.Height = 10
box.Width = 30
doc.recompute()

input('Press Enter to set the Visualization!.. ')

## A.4. Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
doc.recompute()

input('Press Enter to color the box!.. ')

#######
box = doc.getObject('MyBox')
rRed = random.random()
rGreen = random.random()
rBlue = random.random()
print(f'{rRed} {rGreen} {rBlue}')
box.ViewObject.ShapeColor = (rRed, rGreen, rBlue)
#######

## A.5. Selecting the box previously created
selectedObj = doc.getObject('MyBox')
selectedObjPla = selectedObj.Placement
selectedObjPlaMat = selectedObjPla.toMatrix()


## A.6. Obtaining the existing box placement values as Matrix
startingX = selectedObjPlaMat.A14
startingY = selectedObjPlaMat.A24
startingZ = selectedObjPlaMat.A34

## A.7. Preparing the position parameters with factor variable
factor = 3
newX = startingX + factor
newY = startingY + factor
newZ = startingZ + factor

input('Press Enter to move box')

### B. MATRIX TRANFORMATIONS #####################
## B.1. Translating or Moving
# Moving the box to new placement
selectedObjPlaMat.move(newX, newY, newZ)
selectedObj.Placement = selectedObjPlaMat
doc.recompute()

input('Press Enter to move the box back!.. ')

# Resetting the box to its original placement
selectedObjPlaMat.A14 = startingX
selectedObjPlaMat.A24 = startingY
selectedObjPlaMat.A34 = startingZ
selectedObj.Placement = App.Placement(App.Vector(startingX, startingY, startingZ), App.Rotation())
doc.recompute()

input('Press Enter to rotate the box!.. ')

## B.2. Rotating
# Rotating around X axis
angle = 45
selectedObjPlaMat.rotateX(angle)
selectedObj.Placement = App.Placement(selectedObjPlaMat)
doc.recompute()

input('Press Enter to rotate the box to its previous position!..')

# undo rotateX operation
selectedObjPlaMat.rotateX(-angle)
selectedObj.Placement = App.Placement(selectedObjPlaMat)
doc.recompute()

input('Press Enter to scale the box!..')

## B.3. Scaling
# Accessing and copying the shape
shape = box.Shape.copy()

# Create a scaling matrix
scale_matrix = App.Matrix()
scale_matrix.A11 = 2  # Scale X by 2
scale_matrix.A22 = 2  # Scale Y by 2
scale_matrix.A33 = 0.5  # Scale Z by 1

# Apply the scaling matrix to the shape
scaled_shape = shape.transformGeometry(scale_matrix)

# Add the scaled shape to the document
scaled_box = doc.addObject("Part::Feature", "ScaledBox")
scaled_box.Shape = scaled_shape
doc.recompute()

### C. HIDING AND SHOWING OBJECTS #############
input('Press Enter to hide the source box!..')

# Hiding the source box
selectedObj = doc.getObject('MyBox')
selectedObj.ViewObject.hide()

input('Press Enter to hide the scaled box!..')

# Hiding the scaled box
selectedObj = doc.getObject('ScaledBox')
selectedObj.ViewObject.hide()

input('Press Enter to show the source box!..')

# Showing the source box
selectedObj = doc.getObject('MyBox')
selectedObj.ViewObject.show()

input('Press Enter to show the scaled box!..')

# Showing the scaled box
selectedObj = doc.getObject('ScaledBox')
selectedObj.ViewObject.show()




