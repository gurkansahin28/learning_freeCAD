#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:30:45 2024

@author: gurkan
"""

import FreeCAD as App
import FreeCADGui as Gui
import Draft
#########################################
docName = 'SquareFromJoinedWires'
doc = App.newDocument(docName)
#########################################
z = 0
units = 10
###
wire1V1 = App.Vector(0, 0, z)
wire1V2 = App.Vector(0, units, z)
wire1 = Draft.makeWire([wire1V1, wire1V2])

wire2V2 = App.Vector(units, units, z)
wire2 = Draft.makeWire([wire1V2, wire2V2])

wire3V2 = App.Vector(units, 0, z)
wire3 = Draft.makeWire([wire2V2, wire3V2])

wire4 = Draft.makeWire([wire3V2, wire1V1])
###
doc.recompute()
###
wiresList = [wire1, wire2, wire3, wire4]
joinedWires = Draft.upgrade(wiresList, delete = True)[0]
doc.recompute()
##########################################
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
##########################################
