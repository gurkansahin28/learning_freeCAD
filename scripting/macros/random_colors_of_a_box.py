#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:22:36 2024

@author: gurkan
"""

# importing PySide for a simple dialog
from PySide import QtGui
# importing freecad and the gui as aliases
import FreeCAD as App
import FreeCADGui as Gui
import random


####################################################
### DOCUMENT AND A BOX #############################
####################################################
# checking existing document, otherwise creating one
if not App.ActiveDocument:
    docName = 'RandomlyColourisingDoc'
    doc = App.newDocument(docName)
    doc.recompute()
else:
    #### !!! note: these two lines should be review
    #### because it can not be handled box object
    doc = App.ActiveDocument
    box = doc.ActiveObject

# adding a box to the document
box = doc.addObject('Part::Box', 'RandColorBox')
doc.recompute()

# setting up the visualization
Gui.activeDocument().activeView().viewAxometric()
Gui.runCommand('Draft_ToggleGrid', 0)
Gui.ActiveDocument.ActiveView.setAxisCross(True)
Gui.SendMsgToActiveView('ViewFit')

###################################################
### SIMPLE DIALOG WINDOW WIDGETS ##################
###################################################

def randomlyColorize():
    randRed = random.random()
    randGreen = random.random()
    randBlue = random.random()
    box.ViewObject.ShapeColor = (randRed, randGreen, randBlue)
    doc.recompute()
    pass
#----------------------------------------------

class OkCancelWindow(QtGui.QWidget):
    def __init__(self):
        super(OkCancelWindow, self).__init__()

        # setting window properties
        self.setWindowTitle('Colorize It?...')
        # gettting the parent geometry
        parent = QtGui.QApplication.activeWindow()
        pGeo = parent.geometry()
        pGeoX = pGeo.x()
        pGeoY = pGeo.y()
        # setting the child window geometry
        factor = 50
        childGeoX = pGeoX + 3*factor
        childGeoY = pGeoY + factor
        width = 250
        height = 200
        self.setGeometry(childGeoX, childGeoY, width, height)

        # creating layout
        layout = QtGui.QVBoxLayout()

        # creating fields
        labelAbout = QtGui.QLabel('Short Info:\nTo color the Cube press \'Yes!\'...')
        layout.addWidget(labelAbout)

        buttonOk = QtGui.QPushButton('Yes!')
        buttonOk.clicked.connect(randomlyColorize)
        layout.addWidget(buttonOk)

        buttonNo = QtGui.QPushButton('No!')
        buttonNo.clicked.connect(self.close)
        layout.addWidget(buttonNo)

        self.setLayout(layout)

window = OkCancelWindow()
window.show()
#################################################
### RANDOMLY COLORIZE FUNCTION ##################
#################################################
def randomlyColorize():
    randRed = random.random()
    randGreen = random.random()
    randBlue = random.random()
    box.ViewObject.ShapeColor = (randRed, randGreen, randBlue)
    doc.recompute()
    pass

