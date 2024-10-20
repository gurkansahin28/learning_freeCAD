#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:53:55 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import PartDesign
import Sketcher

##################################################
# Ensure the PartDesign Workbench is active
Gui.activateWorkbench('PartDesignWorkbench')

# Create a new document
docName = "SketchToExtrude"
doc = App.newDocument(docName)
Gui.activeDocument().activeView().viewAxometric()

# Add a PartDesign Body
body = doc.addObject('PartDesign::Body', 'MyBody')
doc.recompute()

# Add a Sketch inside the MyBody
sketch = doc.addObject('Sketcher::SketchObject', 'MySketch')
body.addObject(sketch)

# Set the sketch's plane relative to the MyBody's XY plane
sketch.Support = (body.Origin.OriginFeatures[0], [''])
sketch.MapMode = 'ObjectXY'

# Remove any existing geometry in the sketch (if any)
for i in reversed(range(len(sketch.Geometry))):
    sketch.delGeometry(i)

# Define the geometry of the Sketch (a simple rectangle)
# Add four lines to create a rectangle
sketch.addGeometry(Part.LineSegment(App.Vector(0, 0, 0), App.Vector(10, 0, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(10, 0, 0), App.Vector(10, 10, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(10, 10, 0), App.Vector(0, 10, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(0, 10, 0), App.Vector(0, 0, 0)), False)

# Recompute to apply the sketch
doc.recompute()

#######################
# Add a Pad (extrusion) to the Sketch
pad = doc.addObject('PartDesign::Pad', 'MyPad')
pad.Profile = sketch  # Reference the Sketch for the Pad
pad.Length = 10  # Extrusion height
pad.Length2 = 0  # Optional: second length if symmetric extrusion
pad.Midplane = False  # Whether to extrude symmetrically
pad.Reversed = False  # Whether to reverse the direction of extrusion

# Add the Pad to the Body
body.addObject(pad)

# Recompute the document to apply all changes
doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)