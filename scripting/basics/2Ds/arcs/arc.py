#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:15:34 2024

@author: gurkan
"""
import FreeCAD as App
import FreeCADGui as Gui
import Part
#--------------------------------------------
docName = 'ArcDocument'
doc = App.newDocument(docName)

sketch = doc.addObject('Sketcher::SketchObject', 'ArcSketch')

radius = 2
center = App.Vector(2, 10, 0)
axis = App.Vector(0, 0, 1)
circle = Part.Circle(center, axis, radius)

startAngle = 1.570796
endAngle = 3.132313
arcOfCircle = Part.ArcOfCircle(circle, startAngle, endAngle)
addArcGeo = sketch.addGeometry(arcOfCircle, False)
doc.recompute()
#-------------------------------------------
Gui.SendMsgToActiveView('ViewFit')
