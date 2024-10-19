#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:09:40 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Draft

#################################################
docName = "MakingAPolygon"
doc = App.newDocument(docName)
#####
rad = 100
hexagon = Draft.make_polygon(6, radius= rad)
hexagon.Label = "Hexagon"
pentagon = Draft.make_polygon(5, radius= rad)
pentagon.Label = "Pentagon"
tetragon = Draft.make_polygon(4, radius= rad)
tetragon.Label = "Tetragon"
triangle = Draft.make_polygon(3, radius= rad)
triangle.Label = "Triangle"

doc.recompute()

#polyGonList = [hexagon, pentagon, tetragon, triangle]
moveFactor = rad + 5
Draft.move(hexagon, App.Vector(-moveFactor, 0, 0))
Draft.move(pentagon, App.Vector(moveFactor, 0, 0))
Draft.move(tetragon, App.Vector(2*moveFactor, 0, rad/2))
Draft.move(triangle, App.Vector(0, moveFactor, rad))

doc.recompute()

##################################################
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
# doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
