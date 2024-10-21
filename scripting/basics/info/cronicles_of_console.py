#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:37:57 2024

@author: gurkan
"""

# Gui.runCommand('Std_Workbench',14)
# Gui.runCommand('Std_ViewStatusBar',1)
# Gui.runCommand('Std_Workbench',1)
# Gui.runCommand('Std_Workbench',7)
# Gui.runCommand('Std_Workbench',12)
# Gui.runCommand('Std_Workbench',14)
docName = "Naming"
doc = App.newDocument(docName)
# App.setActiveDocument("Naming")
# App.ActiveDocument=App.getDocument("Naming")
# Gui.ActiveDocument=Gui.getDocument("Naming")
# Gui.runCommand('Std_OrthographicCamera',1)
doc2 = FreeCAD.newDocument(docName)
# App.setActiveDocument("Naming1")
# App.ActiveDocument=App.getDocument("Naming1")
# Gui.ActiveDocument=Gui.getDocument("Naming1")
### FreeCAD = App
doc.addObject('Part::Box', 'MyBox')
doc.ActiveObject.Length=10
doc.ActiveObject.Width=10
doc.ActiveObject.Height=10
doc.recompute()
### Begin command Std_ViewFitAll
# Gui.SendMsgToActiveView("ViewFit")
### End command Std_ViewFitAll
### Begin command Std_ViewFitAll
# Gui.SendMsgToActiveView("ViewFit")
### End command Std_ViewFitAll
# Gui.Selection.addSelection('Naming','MyBox')
# App.setActiveDocument("Naming")
# App.ActiveDocument=App.getDocument("Naming")
# Gui.ActiveDocument=Gui.getDocument("Naming")
### Begin command Std_ViewFitAll
# Gui.SendMsgToActiveView("ViewFit")
### End command Std_ViewFitAll
### Begin command Std_ViewIsometric
# Gui.activeDocument().activeView().viewIsometric()
### End command Std_ViewIsometric
# Gui.Selection.clearSelection()
App.ActiveDocument.clearDocument()
# App.setActiveDocument("")
# App.ActiveDocument=None
# Gui.ActiveDocument=None
# App.setActiveDocument("Naming1")
# App.ActiveDocument=App.getDocument("Naming1")
# Gui.ActiveDocument=Gui.getDocument("Naming1")
App.closeDocument(App.activeDocument)
App.closeDocument("Naming1")
# App.setActiveDocument("")
# App.ActiveDocument=None
# Gui.ActiveDocument=None
#####################################################################
App.closeDocument("Naming")
box = doc.addObject('Part::Box', 'MyBox')
box.Name
if box.Name == 'MyBox':
	print('it is')

doc.ActiveObject.Name
doc.Objects
doc.Objects[0]
doc.Objects[1]
>>> doc.Objects[1]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range
>>> 
>>> print('I am sorry! It is my mistake!')
I am sorry! It is my mistake!
>>> print('It was just a humble and simply try')
It was just a humble and simply try
>>> 
#######################################################################
>>> Gui.runCommand('Std_Workbench',1)
>>> # Gui.activateWorkbench("DraftWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 2)
>>> # Gui.activateWorkbench("FemWorkbench")

>>> Gui.runCommand('Std_Workbench', 3)
>>> # Gui.activateWorkbench("InspectionWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 4)
>>> # Gui.activateWorkbench("MeshWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 5)
>>> # Gui.activateWorkbench("OpenSCADWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 6)
>>> # Gui.activateWorkbench("PartDesignWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench',7)
>>> # Gui.activateWorkbench("PartWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 8)
>>> # Gui.activateWorkbench("PathWorkbench")
>>> import PartDesignGui
>>> 
>>> Gui.runCommand('Std_Workbench', 9)
>>> # Gui.activateWorkbench("PointsWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 10)
>>> # Gui.activateWorkbench("ReverseEngineeringWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 11)
>>> # Gui.activateWorkbench("RobotWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench',12)
>>> # Gui.activateWorkbench("SketcherWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 13)
>>> # Gui.activateWorkbench("SpreadsheetWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench',14)
>>> # Gui.activateWorkbench("StartWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 15)
>>> # Gui.activateWorkbench("SurfaceWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 16)
>>> # Gui.activateWorkbench("TechDrawWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 17)
>>> # Gui.activateWorkbench("WebWorkbench")
>>> 
>>> Gui.runCommand('Std_Workbench', 18)
### FreeCAD quited apruptly.....
