#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:07:42 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Draft

docName = 'RoundedBoxXY'
doc = App.newDocument(docName)

### SETTING XY ###
z = 0.0
pl = App.Placement()
pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)

### SPECIFIC DIMENTIONS OF THE RECT ###
# width and height
sx = 260.0 # width
sy = 355.0 # height

# r for radius to round the rectangle
r = 5.0

# the difference along X axis
dx = sx - r

# the difference along Y axis
dy = sy - r


### CENTER VECTORS FOR ROUNDING ######
# the center of the left bottom arc
clba = App.Vector(r, r, z)

# the center of the left top arc
clta = App.Vector(r, dy, z)

# the center of the right top arc
crta = App.Vector(dx, dy, z)

# the center of the rigth bottom arc
crba = App.Vector(dx, r, z)


### WIRE VECTORS FOR THE EDGES #########
# the left wire vectors of the left edge
lwV1 = App.Vector(0, r, z) # Vector 1
lwV2 = App.Vector(0, dy, z) # Vector 2
lwVectors = [lwV1, lwV2]

# the top wire vectors of the top edge
twV1 = App.Vector(r, sy, z)
twV2 = App.Vector(dx, sy, z)
twVectors = [twV1, twV2]

# the right wire vectors of the right edge
rwV1 = App.Vector(sx, dy, z)
rwV2 = App.Vector(sx, r, z)
rwVectors = [rwV1, rwV2]

# the bottom wire vectors of the bottom edge
bwV1 = App.Vector(dx, 0, z)
bwV2 = App.Vector(r, 0, 0)
bwVectors = [bwV1, bwV2]


### DRAWING OF THE ARCS AND WIRES ###
# the left bottom arc
pl.Base = clba
start = 180.0
end = 270.0
lba = Draft.make_circle(radius = r, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
doc.recompute()
# the left wire
lw = Draft.makeWire(lwVectors)
doc.recompute()

# the left top arc
pl.Base = clta
start = 90.0
end = 180.0
lta = Draft.make_circle(radius = r, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
doc.recompute()
# the top wire
tw = Draft.makeWire(twVectors)
doc.recompute()

# the right top arc
pl.Base = crta
start = 0.0
end = 90.0
rta = Draft.make_circle(radius = r, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
doc.recompute()
# the right wire
rw = Draft.makeWire(rwVectors)
doc.recompute()

# the right bottom arc
pl.Base = crba
start = 270.0
end = 360.0
rba = Draft.make_circle(radius = r, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
doc.recompute()
# the bottom wire
bw = Draft.makeWire(bwVectors)
doc.recompute()


### JOINING THE WHOLE DRAWING ###
wireList = [lba, lw, lta, tw, rta, rw, rba, bw]
j = Draft.upgrade(wireList, delete = True)[0]
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
