#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:51:43 2024

@author: gurkan
"""

# 260 mm 355 mm 50 mm

import FreeCAD as App
import FreeCADGui as Gui
import Draft

docName = 'RoundedRect'

doc = App.newDocument(docName)

z = 0.0
r = 5.0
pl = App.Placement()
pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)
pl.Base = App.Vector(r, r, z)
start = 180.0
end = 270.0

units_h = 345.0
units_w = 250.0

# LEFT BOTTOM ARC -----------------------------------
arcLeftBottom = Draft.make_circle(radius = r, placement=pl, face=False, startangle=start, endangle=end, support=None)
doc.recompute()

wire1V1 = App.Vector(0.0, r, z)
wire1V2 = App.Vector(0.0, units_h, z)
wire1Vectors = [wire1V1, wire1V2]
wire1 = Draft.makeWire(wire1Vectors)
doc.recompute()

# LEFT TOP ARC --------------------------------------
pl.Base = App.Vector(r, units_h, z)
start = 90
end = 180
arcLeftTop = Draft.make_circle(radius = r, placement=pl, face=False, startangle=start, endangle=end, support=None)
doc.recompute()

wire2V1 = App.Vector(r, (units_h + r), z)
wire2V2 = App.Vector((units_w + r), (units_h + r), z)
wire2Vectors = [wire2V1, wire2V2]
wire2 = Draft.makeWire(wire2Vectors)
doc.recompute()

# RIGHT TOP ARC -------------------------------------
pl.Base = App.Vector((units_w + r), units_h, z)
start = 0
end = 90
arcRightTop = Draft.make_circle(radius = r, placement=pl, face=False, startangle=start, endangle=end, support=None)
doc.recompute()

wire3V1 = App.Vector((units_w + 2*r), units_h, z)
wire3V2 = App.Vector((units_w + 2*r), r, z)
wire3Vectors = [wire3V1, wire3V2]
wire3 = Draft.makeWire(wire3Vectors)
doc.recompute()

# RIGHT BOTTOM ARC ----------------------------------
pl.Base = App.Vector((units_w + r), r, z)
start = 270
end = 360
arcRightBottom = Draft.make_circle(radius = r, placement=pl, face=False, startangle=start, endangle=end, support=None)
doc.recompute()

wire4V1 = App.Vector((units_w + r), 0, z)
wire4V2 = App.Vector(r, 0, z)
wire4Vectors = [wire4V1, wire4V2]
wire4 = Draft.makeWire(wire4Vectors)
doc.recompute()

# UNIFYING THE WHOLE DRAWING ------------------------
wireList = [arcLeftBottom, wire1, arcLeftTop, wire2, arcRightTop, wire3, arcRightBottom, wire4]
joinedWires = Draft.upgrade(wireList, delete = True)[0]
doc.recompute()

##################################################
Gui.activeDocument().activeView().viewTop()
Gui.SendMsgToActiveView('ViewFit')
Gui.ActiveDocument.ActiveView.setAxisCross(True)
###################################################
#Gui.activeDocument().activeView().viewAxometric()
#Gui.activeDocument().activeView().viewIsometric()
#doc.saveAs("/absolute/path/to/your/file.FCStd")
# App.closeDocument(docName)
