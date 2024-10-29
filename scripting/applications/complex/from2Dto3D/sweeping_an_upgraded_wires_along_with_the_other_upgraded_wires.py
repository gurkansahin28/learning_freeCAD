#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:08:59 2024

@author: gurkan
"""
# AN ATTEMPT TO SWEEP AN UPGRADED WIRES ALONG WITH THE OTHER UPGRADED WIRES
import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Part

### NAMING THE DOCUMENT ##########################
docName = 'Sweepingsection'
doc = App.newDocument(docName)

### SETTINGS AT THE BEGINNING #####################
pl = App.Placement()
pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)
 
#### MAKING THE SECTION ############################
# the section wires' vectors ###

# section wire1 vectors
sw1V1 = App.Vector(0, 0, 0)
sw1V2 = App.Vector(0, 5, 0)
sw1Vs = [sw1V1, sw1V2]
sw1 = Draft.makeWire(sw1Vs)
doc.recompute()

# section wire2 vectors
sw2V1 = sw1V2
sw2V2 = App.Vector(8, 5, 0)
sw2Vs = [sw2V1, sw2V2]
sw2 = Draft.makeWire(sw2Vs)
doc.recompute()

# section wire3 vectors
sw3V1 = sw2V2
sw3V2 = App.Vector(8, 0, 0)
sw3Vs = [sw3V1, sw3V2]
sw3 = Draft.makeWire(sw3Vs)
doc.recompute()

# section wire4 vectors
sw4V1 = sw3V2
sw4V2 = App.Vector(6, 0, 0)
sw4Vs = [sw4V1, sw4V2]
sw4 = Draft.makeWire(sw4Vs)
doc.recompute()

# section wire5 vectors
sw5V1 = sw4V2
sw5V2 = App.Vector(6, 3, 0)
sw5Vs = [sw5V1, sw5V2]
sw5 = Draft.makeWire(sw5Vs)
doc.recompute()

# section wire6 vectors
sw6V1 = sw5V2
sw6V2 = App.Vector(2, 3, 0)
sw6Vs = [sw6V1, sw6V2]
sw6 = Draft.makeWire(sw6Vs)
doc.recompute()

# section wire7 vectors
sw7V1 = sw6V2
sw7V2 = App.Vector(2, 0, 0)
sw7Vs = [sw7V1, sw7V2]
sw7 = Draft.makeWire(sw7Vs)
doc.recompute()

# section wire8 vectors
sw8V1 = sw7V2
sw8V2 = sw1V1
sw8Vs = [sw8V1, sw8V2]
sw8 = Draft.makeWire(sw8Vs)
doc.recompute()

###################################################
# section wires joining
swList = [sw1, sw2, sw3, sw4, sw5, sw6, sw7, sw8]
swj = Draft.upgrade(swList, delete = True)[0][0]
#swj = Draft.upgrade(swList, delete = True)[0]
doc.recompute()

###################################################
#### MAKING THE PATH ############################
# the path wires' vectors ###

# path wire1 vectors
pw1V1 = App.Vector(0, 0, 0)
pw1V2 = App.Vector(0, 0, 25)
pw1Vs = [pw1V1, pw1V2]
pw1 = Draft.makeWire(pw1Vs)
doc.recompute()

# path wire2 vectors
pw2V1 = pw1V2
pw2V2 = App.Vector(0, 15, 25)
pw2Vs = [pw2V1, pw2V2]
pw2 = Draft.makeWire(pw2Vs)
doc.recompute()

###################################################
# path wires joining
pwList = [pw1, pw2]
pwj = Draft.upgrade(pwList, delete = True)[0][0]
#pwj = Draft.upgrade(pwList, delete = True)[0]

###################################################

# Setting up the sweep operation
sweep = doc.addObject('Part::Sweep', 'Sweeping')
sweep.Sections = doc.getObject('Wire')
sweep.Spine = doc.getObject('Wire001')
sweep.Solid = True
sweep.Frenet = False
doc.recompute()

#######################################################
Gui.SendMsgToActiveView('ViewFit')













