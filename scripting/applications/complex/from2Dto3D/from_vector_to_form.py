#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:20:03 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui

V1 = App.Vector(0, 10, 0)
V2 = App.Vector(30, 10, 0)
V3 = App.Vector(30, -10, 0)
V4 = App.Vector(0, -10, 0)

L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V4, V3)

VC1 = App.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)

VC2 = App.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)

E1 = Part.Edge(L1)
E2 = Part.Edge(L2)
E3 = Part.Edge(C1)
E4 = Part.Edge(C2)

W = Part.Wire([E1, E4, E2, E3])

# print(W.isClosed())

F = Part.Face(W)
P = F.extrude(App.Vector(0, 0, 10))

#print(P.ShapeType)

docName = 'FromVectorToForm'
doc = App.newDocument(docName)

myObject = doc.addObject('Part::Feature', 'VecToFo')
myObject.Shape = P
doc.recompute()

Gui.SendMsgToActiveView('ViewFit')
Gui.activeDocument().activeView().viewAxometric()
Gui.ActiveDocument.ActiveView.setAxisCross(True)
