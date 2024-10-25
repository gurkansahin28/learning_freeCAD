#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:37:05 2024

@author: gurkan
"""

from PySide import QtGui
import FreeCAD as App
import FreeCADGui as Gui
import Draft

# Define the main window
class DataEntryWindow(QtGui.QWidget):
    def __init__(self):
        super(DataEntryWindow, self).__init__()
        
        # Set window properties
        self.setWindowTitle("Rounded Rect XY Entries")
        self.setGeometry(100, 100, 300, 300)

        # Create layout
        layout = QtGui.QVBoxLayout()

        # Create input fields with labels
        self.sxLabel = QtGui.QLabel("Enter Width:")
        self.sxInput = QtGui.QLineEdit()
        
        self.syLabel = QtGui.QLabel("Enter Height:")
        self.syInput = QtGui.QLineEdit()
        
        self.srLabel = QtGui.QLabel("Enter Radius:")
        self.srInput = QtGui.QLineEdit()
        
        # Create buttons
        self.submit_button = QtGui.QPushButton("Submit")
        self.submit_button.clicked.connect(self.process_data)

        self.clear_button = QtGui.QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_data)
        
        self.close_button = QtGui.QPushButton("Cancel")
        self.close_button.clicked.connect(self.close)

        # Add widgets to layout
        layout.addWidget(self.sxLabel)
        layout.addWidget(self.sxInput)
        layout.addWidget(self.syLabel)
        layout.addWidget(self.syInput)
        layout.addWidget(self.srLabel)
        layout.addWidget(self.srInput)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.close_button)
        
        self.setLayout(layout)

    def process_data(self):
        # Get data from inputs
        sxi = self.sxInput.text()
        syi = self.syInput.text()
        sri = self.srInput.text()
        
        # Evaluate and display a message based on data
        try:
            sxf = float(sxi)
            syf = float(syi)
            srf = float(sri)
            message = f"Width: {sxf}, Heigth: {syf} and Radius: {srf}."
            roundedRectXY(sxf, syf, srf)
        except ValueError:
            message = "Please, enter integers or floats."
            print(message)
        #QtGui.QMessageBox.information(self, "Data Output", message)

    def clear_data(self):
        # Clear the input fields
        self.sxInput.clear()
        self.syInput.clear()
        self.srInput.clear()

# Show the data entry window
window = DataEntryWindow()
window.show()


def roundedRectXY(x, y, r):

    if not App.ActiveDocument:
        docName = "RoundedRectXY"
        doc = App.newDocument(docName)
    else:
        doc = App.ActiveDocument
    
    ### SETTING XY ###
    z = 0
    sx = x
    sy = y
    sr = r
    pl = App.Placement()
    pl.Rotation.Q = (0.0, -0.0, -0.0, 1.0)
    
    ### SPECIFIC DIMENTIONS OF THE RECT ###
    # the difference along X axis
    dx = sx - sr

    # the difference along Y axis
    dy = sy - sr
    
 
    ### CENTER VECTORS FOR ROUNDING ######
    # the center of the left bottom arc
    clba = App.Vector(sr, sr, z)

    # the center of the left top arc
    clta = App.Vector(sr, dy, z)

    # the center of the right top arc
    crta = App.Vector(dx, dy, z)

    # the center of the rigth bottom arc
    crba = App.Vector(dx, sr, z)   


    ### WIRE VECTORS FOR THE EDGES #########
    # the left wire vectors of the left edge
    lwV1 = App.Vector(0, sr, z) # Vector 1
    lwV2 = App.Vector(0, dy, z) # Vector 2
    lwVectors = [lwV1, lwV2]

    # the top wire vectors of the top edge
    twV1 = App.Vector(sr, sy, z)
    twV2 = App.Vector(dx, sy, z)
    twVectors = [twV1, twV2]

    # the right wire vectors of the right edge
    rwV1 = App.Vector(sx, dy, z)
    rwV2 = App.Vector(sx, sr, z)
    rwVectors = [rwV1, rwV2]

    # the bottom wire vectors of the bottom edge
    bwV1 = App.Vector(dx, 0, z)
    bwV2 = App.Vector(sr, 0, 0)
    bwVectors = [bwV1, bwV2]
    
    
    ### DRAWING OF THE ARCS AND WIRES ###
    # the left bottom arc
    pl.Base = clba
    start = 180.0
    end = 270.0
    lba = Draft.make_circle(radius = sr, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
    doc.recompute()
    # the left wire
    lw = Draft.makeWire(lwVectors)
    doc.recompute()

    # the left top arc
    pl.Base = clta
    start = 90.0
    end = 180.0
    lta = Draft.make_circle(radius = sr, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
    doc.recompute()
    # the top wire
    tw = Draft.makeWire(twVectors)
    doc.recompute()

    # the right top arc
    pl.Base = crta
    start = 0.0
    end = 90.0
    rta = Draft.make_circle(radius = sr, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
    doc.recompute()
    # the right wire
    rw = Draft.makeWire(rwVectors)
    doc.recompute()

    # the right bottom arc
    pl.Base = crba
    start = 270.0
    end = 360.0
    rba = Draft.make_circle(radius = sr, placement = pl, face = False, 
                        startangle = start, endangle = end, support = None)
    doc.recompute()
    # the bottom wire
    bw = Draft.makeWire(bwVectors)
    doc.recompute()


    ### JOINING THE WHOLE DRAWING ###
    wireList = [lba, lw, lta, tw, rta, rw, rba, bw]
    j = Draft.upgrade(wireList, delete = True)[0]
    doc.recompute()
    
    #App.ActiveDocument.ActiveObject.Label = f'RoundedDraft{lw}x{tw}_{lba}'
    App.ActiveDocument.ActiveObject.Label = f'Rounded_{int(sx)}x{int(sy)}-{int(sr)}'
    # Gui.Selection.clearSelection()

    ##################################################
    Gui.activeDocument().activeView().viewTop()
    Gui.SendMsgToActiveView('ViewFit')
    Gui.ActiveDocument.ActiveView.setAxisCross(True)
    pass

